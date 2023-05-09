from socket import *
import random
import time

BUFSIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

while True:
    s_sock.settimeout(None)
    while True:
        data, addr = s_sock.recvfrom(BUFSIZE)
        if random.random() <= 0.5:
            continue
        else:
            s_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
        
    msg = input('-> ')
    reTx = 0

    while reTx <= 5:
        reps = str(reTx) + ' ' + msg
        s_sock.sendto(reps.encode(), addr)
        s_sock.settimeout(2)

        try:
            data, addr = s_sock.recvfrom(BUFSIZE)
        except timeout:
            reTx +=1
            continue
        else: 
            break

    