from socket import *
import threading
from datetime import datetime

port = 3335
BUFSIZE = 1024
clients = []
id_dic = {}

class myThread(threading.Thread):
    def __init__(self, conn, addr, data):
        super().__init__()
        self.conn = conn
        self.addr = addr
    
    def run(self)

def recvTask(conn, addr):
    while True:
        data = conn.recv(BUFSIZE)
        if not data: 
            break

        if 'quit' in data.decode():
            if addr in clients:
                print(addr, 'exited')
                clients.remove(addr)
                continue
        
        th = myThread(conn, addr, data.decode)
        th.start()

        if addr not in clients:
            clients.append(addr)
            id = '[' + data.decode() + ']'
            id_dic[addr] = id
            conn.send(id.encode())
            print(clients)
            print(id_dic)
        
        for i in clients:
            if addr != i:
                now = datetime.now()
                year = now.year
                month = now.month
                day = now.day
                weekday = now.strftime("%A")
                time = now.strftime("%H:%M:%S")
                msg = id_dic[addr] + data.decode()
                print('{} {} {} {} {} ({}):{}' .format(weekday, month, day, time, year, addr, msg))
                conn.send(msg.encode())
                print(msg.encode())
                print(clients)
                print(id_dic)


s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(5)
print('Server Started')

while True:
    conn, addr = s_sock.accept()
    print('new client ({}, {})' .format(conn, addr))
    recvTask(conn, addr)