import socket
import threading

def send_file(filename, host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for incoming connections on {host}:{port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    with open(filename, 'rb') as file:
        chunk = file.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = file.read(1024)
    
    print("File transfer complete.")
    client_socket.close()
    server_socket.close()

def receive_file(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    
    with open('received_file.txt', 'wb') as file:
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            file.write(chunk)
    
    print("File received successfully.")
    
    with open('received_file.txt', 'r') as file:
        print("\nFile contents received:")
        print(file.read())
    
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 12345
    filename = 'example.txt'
    send_file(filename, host, port)

def start_client():
    host = '127.0.0.1'
    port = 12345
    receive_file(host, port)

if __name__ == "__main__":
    choice = input("Enter 'server' to start the server or 'client' to start the client: ").lower()
    
    if choice == 'server':
        start_server()
    elif choice == 'client':
        start_client()
    else:
        print("Invalid choice. Please enter 'server' or 'client'.")
