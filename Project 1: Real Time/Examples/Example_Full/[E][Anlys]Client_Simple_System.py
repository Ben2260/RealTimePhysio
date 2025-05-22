import socket
import sys
import numpy as np
import time
import multiprocessing as mp
from multiprocessing import shared_memory
import csv

def write_average_to_csv(avg, file_name, csv_lock):
    """
    Writes the computed average (an array-like of two values) to a CSV file.
    """
    with csv_lock:
        with open(file_name, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(avg)
        print(f"[ProcAverage] Average written to {file_name}")

def ReceiveProcess(host, port, stop_event, RawLock, DistributorLock, chunk_size, shm_shape, shm_name):
    """
    Connects to a TCP server, receives comma-separated float data, collects a full chunk,
    and writes it to shared memory using consistent lock ordering.
    """
    shm_arry = shared_memory.SharedMemory(name=shm_name)
    shm_np = np.ndarray(shm_shape, dtype=np.float64, buffer=shm_arry.buf)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    temp_arry = []
    print("Process 1: Receiving Data")

    try:
        while not stop_event.is_set():
            # (Optionally block/wait for new data)
            data = client_socket.recv(1024)
            if not data:
                break
            rows = data.decode('utf-8').strip().split('\n')
            for row in rows:
                values = list(map(float, row.split(',')))
                temp_arry.append(values)
                if len(temp_arry) == chunk_size:
                    # Always acquire locks in the same order: DistributorLock then RawLock.
                    DistributorLock.acquire()
                    print("P1 took DistributorLock")
                    RawLock.acquire()
                    print("P1 took RawLock")
                    
                    # Write the new data chunk into shared memory.
                    shm_np[:chunk_size] = temp_arry[:chunk_size]
                    print("P1: Shared Memory Updated")
                    
                    # Release locks in reverse order.
                    RawLock.release()
                    print("P1 released RawLock")
                    DistributorLock.release()
                    print("P1 released DistributorLock")
                    
                    temp_arry = []
    except socket.timeout:
        print("Timeout occurred, no data received within the specified time.")
    except Exception as e:
        print(f"Process 1 produced the following error:\n\n{e}")
    finally:
        client_socket.close()

def ProcSplit(stop_event, RawLock, DistributorLock, shm_shape, shm_name, chunk_size):
    """
    Reads the loaded data chunk from shared memory and splits it into two arrays
    while acquiring locks in a consistent order.
    """
    shm_arry = shared_memory.SharedMemory(name=shm_name)
    shm_np = np.ndarray(shm_shape, dtype=np.float64, buffer=shm_arry.buf)
    print("Process 2: Splitting Data")

    temp_arry = np.zeros(shm_shape, dtype=np.float64)
    eda_data = np.zeros(chunk_size, dtype=np.float64)
    rsp_data = np.zeros(chunk_size, dtype=np.float64)

    try:
        while not stop_event.is_set():
            # Clear arrays
            temp_arry.fill(0)
            eda_data.fill(0)
            rsp_data.fill(0)
            
            # Acquire locks in the same order.
            DistributorLock.acquire()
            print("P2 took DistributorLock")
            RawLock.acquire()
            print("P2 took RawLock")
            
            # Copy the full data chunk.
            temp_arry[:] = shm_np[:]
            
            # Release the locks.
            RawLock.release()
            print("P2 released RawLock")
            DistributorLock.release()
            print("P2 released DistributorLock")
            
            # Split the data into two arrays (one for each column).
            eda_data[:] = temp_arry[:, 0]
            rsp_data[:] = temp_arry[:, 1]
            
            # (Further processing on eda_data and rsp_data can be done here.)
            time.sleep(0.5)  # Optional delay to slow down busy-looping.
    except Exception as e:
        print(f"Process 2 produced the following error:\n\n{e}")
    finally:
        print("Process 2 finished.")

def ProcAverage(stop_event, RawLock, DistributorLock, shm_shape, shm_name, chunk_size, csv_lock):
    """
    Reads the shared memory data chunk, computes the column-wise average,
    prints the result, and writes it to a CSV file named "Example product csv.csv".
    """
    shm_arry = shared_memory.SharedMemory(name=shm_name)
    shm_np = np.ndarray(shm_shape, dtype=np.float64, buffer=shm_arry.buf)
    print("Process 3: Average Calculation")

    try:
        while not stop_event.is_set():
            # Acquire locks in the same order.
            DistributorLock.acquire()
            print("P3 took DistributorLock")
            RawLock.acquire()
            print("P3 took RawLock")
            
            # Make a local copy of the current data chunk.
            local_chunk = np.copy(shm_np[:chunk_size])
            
            RawLock.release()
            print("P3 released RawLock")
            DistributorLock.release()
            print("P3 released DistributorLock")
            
            # Compute the column-wise average.
            avg = np.mean(local_chunk, axis=0)
            print("Process 3: Average of loaded chunk:", avg)
            
            # Write the average to a CSV file.
            write_average_to_csv(avg, "Example_product_csv.csv", csv_lock)
            
            time.sleep(1)  # Pause before processing the next chunk.
    except Exception as e:
        print(f"Process 3 produced the following error:\n\n{e}")
    finally:
        print("Process 3 finished.")

if __name__ == '__main__':

    host = 'localhost'
    port = 12345

    ExamLimit = 1000  # Number of rows per data chunk.
    shape = (ExamLimit, 2)
    dtype = np.float64

    # Locks for synchronizing shared memory and CSV access.
    RawLock = mp.Lock()
    DistributorLock = mp.Lock()
    csv_lock = mp.Lock()
    stop_event = mp.Event()

    # Create shared memory.
    shm = shared_memory.SharedMemory(create=True, size=int(np.prod(shape) * np.dtype(dtype).itemsize))
    shared_array = np.ndarray(shape, dtype=dtype, buffer=shm.buf)

    # Create processes.
    p1 = mp.Process(target=ReceiveProcess, args=(host, port, stop_event, RawLock, DistributorLock,
                                                   ExamLimit, shape, shm.name))
    p2 = mp.Process(target=ProcSplit, args=(stop_event, RawLock, DistributorLock, shape, shm.name, ExamLimit))
    p3 = mp.Process(target=ProcAverage, args=(stop_event, RawLock, DistributorLock, shape, shm.name, ExamLimit, csv_lock))

    try:
        # Start processes.
        p1.start()
        time.sleep(0.1)  # Ensure Process 1 initializes first.
        p2.start()
        p3.start()

        # Keep the main process running.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Ctrl+C] detected! Cleaning up...")

        # Signal all processes to stop.
        stop_event.set()
        p1.join(timeout=5)
        print("Force killing Process 1..." if p1.is_alive() else "Process 1 terminated.")
        p2.join(timeout=5)
        print("Force killing Process 2..." if p2.is_alive() else "Process 2 terminated.")
        p3.join(timeout=5)
        print("Force killing Process 3..." if p3.is_alive() else "Process 3 terminated.")
        if p1.is_alive():
            p1.terminate()
        if p2.is_alive():
            p2.terminate()
        if p3.is_alive():
            p3.terminate()

        # Clean up shared memory.
        try:
            shm.close()
            shm.unlink()
            print("Clearing Memory")
        except Exception as e:
            print(f"Error cleaning shared memory: {e}")

        print("All processes terminated and shared memory cleaned up. Exiting...")
        sys.exit(0)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        stop_event.set()
        time.sleep(0.1)
        p1.terminate()
        p2.terminate()
        p3.terminate()
        time.sleep(0.1)
        shm.close()
        shm.unlink()
        sys.exit(1)
