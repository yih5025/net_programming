from socket import *
import threading

port = 3333
BUFSIZE = 1024

def sendTask(sock):
    while True:
        resp = input()
        print('-> ', resp)
        sock.send(resp.encode())

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()

th = threading.Thread(target=sendTask, args=(conn,))
th.start()

while True:
    data = conn.recv(BUFSIZE)
    print('<- ', data.decode())

    