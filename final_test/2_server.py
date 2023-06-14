from socket import *
import threading

port = 7777
BUFSIZE = 1024
dic = {}
cube1 = []
cube2 = []

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            data = self.conn.recv(BUFSIZE)
            if not data:
                break
            
            print(data.decode())
            msg = data.decode().split()

            if msg[0] == '1':
                cube1.append(msg[1])
                dic[msg[0]] = cube1
            elif msg[0] == '2':
                cube2.append(msg[1])
                dic[msg[0]] = cube2
                
            print(dic)

            

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(5)
print('Server Started')

lock = threading.Lock()
while True:
    conn, addr = s_sock.accept()
    client_thread = ClientThread(conn, addr)
    client_thread.start()