import socket
import threading

port = 2500
BUFSIZE = 1024

def handler(sock):
    while True:
        msg, addr = sock.recvfrom(BUFSIZE)

svr_addr = ('localhost', port)
c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_sock.connect(('localhost', port))

my_id = input('ID를 입력하세요: ')
c_sock.send(('[' + my_id + ']').encode(), svr_addr)

th = threading.Thread(target=handler, args=(c_sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    c_sock.send(msg.encode(), svr_addr)