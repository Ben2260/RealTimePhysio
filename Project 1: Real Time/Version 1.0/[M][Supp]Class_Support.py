import ast
import time
import numpy as np
import random
import multiprocessing
import matplotlib.pyplot as plt
import importlib
import sys
import os
import socket

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QTextEdit, QPushButton, QMessageBox, QLabel, QListWidget, QFileDialog
)
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class UniqueFunctionProcessor(multiprocessing.Process):
    """
    A process class that processes data from a buffer repeatedly, using a token-passing system.
    """
    def __init__(self, process_id, buffer, __ReadLock, __ReadFlag, result_queue):
        super().__init__()
        self.process_id = process_id  # Unique ID for this process
        self.buffer = buffer  # Shared buffer
        self.ReadLock = __ReadLock  # Mutex lock
        self.ReadFlag = __ReadFlag  # Shared flag to control lock ownership
        self.result_queue = result_queue

    def run(self):
        while True:
            with self.lock:
                # Only proceed if it's this process's turn
                if self.flag.value == self.process_id:
                    if not self.buffer:
                        print(f"Process {self.process_id}: Buffer is empty. Exiting...")
                        break

                    # Consume a data chunk from the buffer
                    data_chunk = self.buffer.pop(0)
                    print(f"Process {self.process_id}: Processing data chunk: {data_chunk}")
                    
                    # Simulate processing and generate a result
                    result = sum(data_chunk)  # Example: Summing the chunk
                    self.result_queue.put((self.process_id, result))
                    print(f"Process {self.process_id}: Processed data chunk. Result: {result}")

                    # Pass control to the next process
                    self.flag.value = ((self.flag.value + 1) % 2)  # Assume 2 processes for simplicity
                    print(f"Set flag to {self.flag.value}")

            time.sleep(0.01)  # Simulate some delay to avoid tight loops


class Echo(multiprocessing.Process):
    """
    A process class responsible for adding new data to the buffer.
    """
    def __init__(self, buffer, lock, flag):
        super().__init__()
        self.buffer = buffer
        self.lock = lock
        self.flag = flag
    def run(self):
        while True:
            with self.lock:
                if len(self.buffer) < 10:  # Prevent buffer overflow
                    new_data = [random.randint(1, 20) for _ in range(3)]
                    print(f"Echo: Adding new data to buffer: {new_data}")
                    self.buffer.append(new_data)
                    self.flag.value = ((self.flag.value + 1) % 2)
                    print(f"Set flag to {self.flag.value}")
            time.sleep(1)  # Simulate delay between additions

class FileManagerWidget(QWidget):
    """Enhanced File Manager Component with Function Extraction"""
    def __init__(self, title, terminal_view):
        super().__init__()
        self.title = title
        self.terminal_view = terminal_view
        self.file_functions = {}  # Display oriented file-function associations sotrage
        self.user_file_functions = []

        # Layout setup
        layout = QVBoxLayout()

        # Section label
        self.label = QLabel(self.title)
        layout.addWidget(self.label)

        # Displayed File list
        self.disp_file_list = QListWidget()
        self.disp_file_list.itemClicked.connect(self.display_functions)
        layout.addWidget(self.disp_file_list)

        # Displayed Function list
        self.disp_function_list = QListWidget()  # Display extracted functions
        self.disp_function_list.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(self.disp_function_list)

        # Add File Button
        self.add_file_button = QPushButton(f"Add {self.title}")
        self.add_file_button.clicked.connect(self.add_file)
        layout.addWidget(self.add_file_button)

        # Save Function Mapping Button
        self.save_button = QPushButton("Save Function Mapping")
        self.save_button.clicked.connect(self.save_mapping)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def add_file(self):
        """Select a file and extract its functions"""
        file_path, _ = QFileDialog.getOpenFileName(self, f"Select {self.title}")
        if file_path is not None:
            functions = self.extract_functions(file_path)
            if functions is not None:
                # Prevent duplicates in file list
                if not self.disp_file_list.findItems(file_path, Qt.MatchExactly):
                    self.disp_file_list.addItem(file_path)
                    self.file_functions[file_path] = functions  # Initially store all extracted functions
                    self.disp_function_list.clear()
                    self.disp_function_list.addItems(functions)
                    self.terminal_view.append(f"[{self.title}_Added] {file_path}")
                        # Example usage:
                    # module_path = "/path/to/neuro_utils.py"
                    # neuro_utils = dynamic_import("neuro_utils", module_path)

                    # data = [your_data_here]
                    # result = neuro_utils.Neuro_RSP_features(data)
                else:
                    self.terminal_view.append(f"[File_Error] {self.title} Already included\n")
            else:
                self.terminal_view.append(f"\tNo Functions Found\n\tNo functions found in {file_path}")

    def display_functions(self, item):
        """Display functions associated with the selected file"""
        file_path = item.text()
        # If a mapping has already been saved, display only the saved functions,
        # otherwise show all extracted functions.
        associated_functions = self.file_functions.get(file_path, [])
        self.disp_function_list.clear()
        if associated_functions:
            self.disp_function_list.addItems(associated_functions)
        else:
            functions = self.extract_functions(file_path)
            self.disp_function_list.addItems(functions)

    def save_mapping(self):
        """Save selected functions to the file mapping"""
        current_item = self.disp_file_list.currentItem()
        print(current_item)
        if current_item is not None:
            file_path = current_item.text()
            selected_functions = [item.text() for item in self.disp_function_list.selectedItems()]
            if selected_functions[0] is not None:
                # Update the mapping with the user-selected functions.
                # Select only one at a time, it wont work right otherwise
                self.user_file_functions.append([file_path,selected_functions[0]])
                self.terminal_view.append(f"[Mapping Saved] {file_path} -> {selected_functions}")
                print(self.user_file_functions[-1])
            else:
                self.terminal_view.append(f"\tWarning\n\tNo {self.title} selected to save mapping!")

        else:
            self.terminal_view.append(f"\tWarning\n\tInvalid {self.title} selected to save mapping!")


    def dynamic_import(module_name, path):
        sys.path.append(os.path.dirname(path))  # Add module directory to path
        module = importlib.import_module(module_name)  # Load module
        importlib.reload(module)  # Reload to ensure latest version is used
        return module
    
    @staticmethod
    def extract_functions(file_path):
        """Extract function names from the given Python file"""
        try:
            with open(file_path, "r") as file:
                tree = ast.parse(file.read())
            return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        except Exception as e:
            return []

class DynamicGraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the widget layout
        self.layout = QVBoxLayout(self)
        
        # Set up Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Container to hold our data
        self.data = []

        # Create and start a QTimer for live updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(1000)  # Update every second

    def update_graph(self):
        # Simulate adding a new random value to the data array
        self.data.append(np.random.randint(0, 100))  # Random value between 0 and 100

        # Keep only the last 10 data points
        recent_data = self.data[-10:]
        
        # Clear the axis and plot the recent data
        self.ax.clear()
        self.ax.plot(recent_data, marker='o', label="Recent 10 Points")
        self.ax.legend()

        # Dynamically adjust y-axis based on the range of recent_data
        if recent_data:
            self.ax.set_ylim(min(recent_data) - 5, max(recent_data) + 5)

        # Redraw the canvas
        self.canvas.draw()
        

def tcp_read_to_shared_array(shared_array, host='', port=9999):
    """
    Listens on the specified TCP port and appends incoming data as strings 
    to the given shared array. This function runs indefinitely until externally terminated.
    
    Args:
        shared_array (multiprocessing.managers.ListProxy): A shared list reference where received data will be added.
        host (str): The hostname or IP address to bind to (default '' binds to all interfaces).
        port (int): The TCP port to listen on (default 9999).
    """
    # Create a TCP socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    print(f"[TCP Reader] Listening on {host if host else 'all interfaces'}:{port}")

    try:
        while True:
            # Accept an incoming connection.
            conn, addr = sock.accept()
            print(f"[TCP Reader] Connection from {addr}")
            while True:
                data = conn.recv(1024)  # Read up to 1024 bytes.
                if not data:
                    # No more data—client closed connection.
                    break
                # Decode data from bytes to string.
                text_data = data.decode('utf-8')
                # Append the received text to the shared array.
                shared_array.append(text_data)
                print(f"[TCP Reader] Received and stored: {text_data}")
            conn.close()
    except KeyboardInterrupt:
        print("\n[TCP Reader] Keyboard interrupt received. Shutting down.")
    finally:
        sock.close()
