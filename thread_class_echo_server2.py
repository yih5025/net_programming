from socket import *
import threading

port = 2500
BUFSIZE = 1024

class ClientThread(threading.Thread):
    def __init__(self, s_sock):
        threading.Thread.__init__(self)
        self.sock = s_sock
    
    def run(self):
        while True: 
            data = self.sock.recv(BUFSIZE)

            if not data:
                break

            print('Recevied message: ', data.decode())
            self.sock.send(data)
        self.sock.close()



s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(5)

while True:
    conn, (remotehost, remoteport) = s_sock.accept()
    print('connected by', remotehost, remoteport)
    th = ClientThread(conn)
    th.start()