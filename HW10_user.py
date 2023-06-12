import selectors
import socket
import time

sel = selectors.DefaultSelector()
clients = {}
counter = 1

def accept(sock, mask):
    global counter
    conn, (remotehost, remoteport) = sock.accept()
    clients[remoteport] = counter
    counter += 1
    print(clients)
    conn.send(b'Register')
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        del clients[conn]
        return
    
    for i in clients:
        if clients[i] == 1:
        # 클라이언트1에 대한 처리
            file_data = time.asctime() + ':' + 'Device1' + ': ' + data.decode() + '\n'
            print(time.asctime() + ':' + 'Device1' + ': ', data.decode())
            with open('data.txt', 'a') as f:
                f.write(file_data)

        if clients[i] == 2:
        # 클라이언트2에 대한 처리
            file_data = time.asctime() + ':' + 'Device2' + ': ' + data.decode() + '\n'
            print(time.asctime() + ':' + 'Device2' + ': ', data.decode())
            with open('data.txt', 'a') as f:
                f.write(file_data)

sock = socket.socket()
sock.bind(('', 2500))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
