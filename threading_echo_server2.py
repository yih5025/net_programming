from socket import *
import threading

port = 2500
BUFSIZE = 1024

def echoTask(sock):
    while True:
        data = sock.recv(BUFSIZE)

        if not data:
            break

        print('Recevied message: ', data.decode())
        sock.send(data)

    sock.close()

sock_s = socket(AF_INET, SOCK_STREAM)
sock_s.bind(('', port))
sock_s.listen(5)

while True:
    conn, (remotehost, remoteport) = sock_s.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Thread(target=echoTask, args=(conn,))
    th.start()