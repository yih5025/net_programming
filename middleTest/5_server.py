import socket
import random
a = 0
b = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8888))

s.listen(5)

while True:
    client, addr = s.accept()
    
    msg = client.recv(12)

    if msg.decode() == '1':
        temp = random.randint(1, 50)

        client.send(temp.to_bytes(4, 'big'))
        client.send(a.to_bytes(4, 'big'))
        client.send(b.to_bytes(4, 'big'))
    elif msg.decode() == '2':
        temp = random.randint(1, 100)

        client.send(a.to_bytes(4, 'big'))
        client.send(temp.to_bytes(4, 'big'))
        client.send(b.to_bytes(4, 'big'))
    elif msg.decode() == '3':
        temp = random.randint(1, 150)

        client.send(a.to_bytes(4, 'big'))
        client.send(b.to_bytes(4, 'big'))
        client.send(temp.to_bytes(4, 'big'))
    
    print(temp)


    client.close()

