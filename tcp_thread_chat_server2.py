from socket import *
import threading
import time

port = 3335
BUFSIZE = 1024
clients = []

class ClientThread(threading.Thread):
    def __init__(self, conn, addr, client_id):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.client_id = client_id
    
    def run(self):
        while True:
            data = self.conn.recv(BUFSIZE)
            if not data:
                break

            if 'quit' in data.decode():
                if self.client_id in clients:
                    print(self.client_id, 'exited')
                    clients.remove(self.client_id)
                    continue

            if self.client_id not in clients:
                print('new client', self.addr)
                clients.append(self.client_id)

            print(time.asctime() + str(self.client_id) + ':' + data.decode())
            
            for client in clients:
                if client != self.client_id:
                    send_message(client, data)

        self.conn.close()

def send_message(client_id, message): #*******개 짜리 중요 함수
    for client_thread in client_threads: #그니까, 아까 만든 스레드 객체 리스트를 순회하면서, 스레드를 하나씩 꺼내서 addr 하고
        #맞으면, 그 스레드 객체에 메세지를 보내는 그래서, UDP 처럼 멀티 채팅이 되는, 즉, 원하는 위치의 클라이언트에게
        #메세지를 뿌려 줄 수 있는 개쩌는 메소드다.
        if client_thread.client_id == client_id:
            client_thread.conn.send(message)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(5)
print('Server Started')

client_threads = []

while True:
    conn, addr = s_sock.accept()
    client_id = addr  # 클라이언트에게 할당된 고유한 ID
    print('new client', addr)
    clients.append(client_id)
    client_thread = ClientThread(conn, addr, client_id)
    client_threads.append(client_thread) #클라이언트 스레드 객체를 리스트에 추가해서 서버에서 실행 중인 각 클라이언트의 스레드를 추적하기 위해 사용
    client_thread.start() #와 그러니까, 스레드 객체를 돌리는데, 그걸 리스트에 저장할 수 있고, 원할 때 참조해서 그 스레드를 찾을 수 있는 미친 기능?!
