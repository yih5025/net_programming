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
        break

    elif dmsg == 'Register':
        while True:
            temperature = random.randint(0, 40)
            humidity = random.randint(0, 100)
            illuminance = random.randint(70, 150)
            msg = 'Temp={}, Humid={}, lilum={}'.format(temperature, humidity, illuminance)
            print(msg)
            c_sock.send(msg.encode())
            time.sleep(3)
