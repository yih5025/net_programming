from socket import *
import random
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 7777))
id = input('ID: ')

while True:

    msg = str(random.randint(1, 40))
    msg2 = id + ' ' + msg
    print(msg2)
    sock.send(msg2.encode())

    time.sleep(5)