import socket
import random
import selectors

host = 'localhost'
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

selector = selectors.DefaultSelector()
selector.register(server_socket, selectors.EVENT_READ)

message_queues = {}  # 소켓별 메시지 큐 딕셔너리

def generate_random_number():
    return random.randint(0, 40)

def generate_random_number2():
    return random.randint(0, 100)

def handle_request(sock):
    data = sock.recv(1024)
    if data:
        received = data.decode()
        if received == '1':
            number = generate_random_number()
            message_queues[sock].append(str(number).encode())
            selector.modify(sock, selectors.EVENT_WRITE)
        elif received == '2':
            number = generate_random_number2()
            message_queues[sock].append(str(number).encode())
            selector.modify(sock, selectors.EVENT_WRITE)
    else:
        selector.unregister(sock)
        sock.close()
        del message_queues[sock]

def handle_response(sock):
    if message_queues[sock]:
        data = message_queues[sock].pop(0)
        sock.send(data)
    else:
        selector.modify(sock, selectors.EVENT_READ)

while True:
    events = selector.select()
    for key, mask in events:
        sock = key.fileobj
        if sock is server_socket:
            client_socket, client_address = server_socket.accept()
            selector.register(client_socket, selectors.EVENT_READ)
            message_queues[client_socket] = []
        elif mask & selectors.EVENT_READ:
            handle_request(sock)
        elif mask & selectors.EVENT_WRITE:
            handle_response(sock)
