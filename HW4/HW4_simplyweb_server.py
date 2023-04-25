from socket import *

s = socket()
s.bind(('http://127.0.0.1', 80))
s.listen(10)
s = socket(AF_INET, SOCK_STREAM)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')