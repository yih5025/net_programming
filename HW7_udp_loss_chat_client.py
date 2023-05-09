from socket import *
import random
import time

BUFSIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
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
            continue
        else:
            if data.decode() == 'ack': 
                break
            else:
                c_sock.sendto(b'Is not ack, Please send ack.', ('localhost', port))
                continue


    c_sock.settimeout(None)
    while True:
        data, addr = c_sock.recvfrom(BUFSIZE)
        if not data :
            continue
        if random.random() <= 0.5:
            continue
        else:
            c_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break