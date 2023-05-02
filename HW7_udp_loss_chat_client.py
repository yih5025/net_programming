from socket import *
import random
import time

BUFSIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    c_sock.settimeout(None)
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        reps = str(reTx) + ' ' + msg
        c_sock.sendto(reps.encode(), ('localhost', port))
        c_sock.settimeout(2)

        try:
            data, addr = c_sock.recvfrom(BUFSIZE)
        except timeout:
            reTx +=1
            print('timeout')
            continue
        else: 
            print(data.decode())
            break

    while True:
        
        data, addr = c_sock.recvfrom(BUFSIZE)
        if random.random() <= 0.5:
            print('메세지 손실')
            continue
        else:
            c_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break