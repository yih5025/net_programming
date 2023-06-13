import socket

host = 'localhost'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    choice = input("Enter '1' for temperature or '2' for humidity (press q to quit): ")
    
    if choice == 'q':
        break
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please enter '1' or '2'.")
        continue

    client_socket.send(choice.encode())

    response = client_socket.recv(1024).decode()
    
    if response:
        print(f"Received: {response}")
    else:
        print("Connection closed by server.")
        break

client_socket.close()
