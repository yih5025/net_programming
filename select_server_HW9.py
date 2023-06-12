import socket
import select
import time 

socks = []
BUFFER = 1024
PORT = 3335

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    r_sock, _, _ = select.select(socks, [], [])
    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('새로운 클라이언트가 접속했습니다:', addr)
        else:
            data = s.recv(BUFFER)
            if not data:
                socks.remove(s)
                continue

            if b'quit' in data:
                print('클라이언트가 종료했습니다:', s.getpeername())
                s.close()
                socks.remove(s)
            else:
                print(time.asctime() + ' ' + str(s.getpeername()) + ': ' + data.decode())
                for client_sock in socks[1:]:  # 첫 번째 소켓은 서버 소켓이므로 제외
                    if client_sock != s:
                        client_sock.send(data)
