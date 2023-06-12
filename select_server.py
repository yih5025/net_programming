import socket, select
import time
socks = []
addrs = []
BUFFER = 1024
PORT = 3335

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT)+' 에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    print(r_sock, w_sock, e_sock)
    for s in r_sock:
        print('s:', s)
        if s == s_sock: 
            #이 부분이 이제 tcp multi 스레드 부분에서 새로운 클라이언트가 있으면 추가 하는 부분이다.
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            addrs.append(addr)
            print('socks: ', socks)
            print('new client', addr)


        else:
            data = s.recv(BUFFER)
            if not data:
                continue

            if 'quit' in data.decode():
                s.close()
                socks.remove(s)

            print(time.asctime() + addr + ':' + data.decode())
            for i in socks:
                if s != c_sock:
                    s.send(data)