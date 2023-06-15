from socket import *
import random

BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(10)

print('divice2 is running...')
client, addr = s.accept()

while True:

    msg = client.recv(BUFSIZE)
    print(msg)
    dmsg = msg.decode()

    if not dmsg:
        print('not msg')
        client.close()
        continue
    elif dmsg == 'quit':
        print('quit!')
        break
    elif dmsg != 'Request':
        client.send(b'send Request or close')
        continue
    elif dmsg == 'Request':
        heartRate = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        calories = random.randint(1000, 4000)
        print(heartRate, steps, calories)
        client.send(heartRate.to_bytes(4, 'big'))
        client.send(steps.to_bytes(4, 'big'))
        client.send(calories.to_bytes(4, 'big'))





