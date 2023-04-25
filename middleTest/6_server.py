import time
from socket import *
import random

port = 7777
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', port))

pong = 'pong'

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    ping = data.decode()
    print(ping)

    if ping == 'ping':
        if random.randint(1, 10) <= 4 :
            sock.sendto('Fail'.encode(), addr)
            continue
        else:
            sock.sendto(pong.encode(), addr)


        
