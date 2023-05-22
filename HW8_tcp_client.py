import socket
import threading

port = 4600
BUFSIZE = 1024

def handler(sock):
    while True:
        msg, addr = sock.recv(BUFSIZE)

svr_addr = ('localhost', port)

while True:
    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.connect(('localhost', port))

    my_id = input('ID를 입력하세요: ')
    c_sock.send(('[' + my_id + ']').encode())
    th = threading.Thread(target=handler, args=(c_sock,))
    th.daemon = True
    th.start()
    while True:
        msg = '[' + my_id + ']' + input()
        c_sock.send(msg.encode())