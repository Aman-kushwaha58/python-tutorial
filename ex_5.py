import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("Server is listening for messages...")
    
    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Message from {client_address}: {message.decode()}")

        if message.decode().lower() == 'exit':
            print("Server is closing the connection.")
            break
        
        response = input("Enter your reply: ")
        server_socket.sendto(response.encode(), client_address)

    server_socket.close()

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    
    while True:
        message = input("Enter your message: ")
        client_socket.sendto(message.encode(), server_address)

        if message.lower() == 'exit':
            print("Exiting chat.")
            break

        response, _ = client_socket.recvfrom(1024)
        print(f"Server says: {response.decode()}")

    client_socket.close()

def main():
    choice = input("Do you want to run as server or client? (s/c): ")
    if choice.lower() == 's':
        server()
    elif choice.lower() == 'c':
        client()
    else:
        print("Invalid choice. Please select 's' for server or 'c' for client.")

if __name__ == "__main__":
    main()
