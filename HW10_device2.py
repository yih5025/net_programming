from socket import *
import random
import time

BUFSIZE = 1024

c_sock = socket(AF_INET, SOCK_STREAM)
c_sock.connect(('localhost', 2500))

while True:
    msg = c_sock.recv(BUFSIZE)
    print(msg)
    dmsg = msg.decode()

    if not dmsg:
        print('not msg')
        break

    elif dmsg == 'Register':
        while True:
            heartRate = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            calories = random.randint(1000, 4000)
            data = 'Heartbeat={}, Steps={}, Cal={}'.format(heartRate, steps, calories)
            print(data)
            c_sock.send(data.encode())
            time.sleep(5)