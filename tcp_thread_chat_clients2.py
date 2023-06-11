from socket import *
import threading

port = 3335
BUFSIZE = 1024
c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(('localhost', port))

my_id = input('ID를 입력하세요: ')
c_sock.send(('[' + my_id + ']').encode())

def handler(c_sock): 
    while True:
        data = c_sock.recv(BUFSIZE)
        print(data.decode())

th = threading.Thread(target=handler, args=(c_sock,))
th.start()

while True:
    msg = ('[' + my_id + ']' + input())
    c_sock.send(msg.encode())