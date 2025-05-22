import socket

# Server details
HOST = 'localhost'
PORT = 12345

try:
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    while True:
        # Receive data from the server
        data = client_socket.recv(1024)  # Buffer size
        if not data:
            print("Connection closed by the server")
            break
        print("Received:", data.decode('utf-8'))

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the socket
    client_socket.close()
    print("Client socket closed")
