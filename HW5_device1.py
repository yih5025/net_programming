from socket import *
import random

BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(10)

print('divice1 is running...')

while True:
    client, addr = s.accept()

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
        temperature = random.randint(0, 40)
        humidity = random.randint(0, 100)
        illuminance = random.randint(70, 150)
        print(temperature, humidity, illuminance)
        client.send(temperature.to_bytes(4, 'big'))
        client.send(humidity.to_bytes(4, 'big'))
        client.send(illuminance.to_bytes(4, 'big'))