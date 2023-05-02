import socket
import time

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 2500))

print('Server Started')

while True:
    data, addr = sock.recvfrom(1024)
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)
            continue

    if addr not in clients:
        print('new client', addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if client != addr:
            sock.sendto(data, client)
