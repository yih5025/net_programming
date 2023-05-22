import socket
import time
import threading

port = 4600
BUFSIZE = 1024
clients = []

def handler(conn, addr):
    newClients(addr)
    while True:
        data = conn.recv(BUFSIZE)
        if not data:
            break
        quit(data, addr)
        print(time.asctime() + str(addr) + ':' + data.decode())
        allSendClients(data, addr)


def quit(data, addr):
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)

def newClients(addr):
    if addr not in clients:
        print('new clients', addr)
        clients.append(addr)

def allSendClients(data, addr):
    for client in clients:
        if client != addr:
            client.send(data.encode())



s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(5)
print('Server started')

while True :
    conn, addr = s_sock.accept()
    th = threading.Thread(target=handler, args=(conn, addr))
    th.daemon = True
    th.start()
s_sock.close()
