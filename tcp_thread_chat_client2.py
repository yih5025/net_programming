from socket import *
import threading

port = 3334
BUFSIZE = 1024

def recvTask(c_sock):
    while True:
        data = c_sock.recv(BUFSIZE)
        print('<- ', data.decode())

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(('localhost', port))

th = threading.Thread(target=recvTask, args=(c_sock,))
th.start()

while True:
    msg = input()
    print('-> ', msg)
    c_sock.send(msg.encode())