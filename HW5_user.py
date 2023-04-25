from socket import *

BUFSIZE = 1024

sock1 = socket(AF_INET, SOCK_STREAM)
sock2 = socket(AF_INET, SOCK_STREAM)
sock1.connect(('localhost', 8888))
sock2.connect(('localhost', 7777))

inputnumber = input('Press 1 or 2 or quit:')
print(inputnumber)

if inputnumber == '1':
    sock1.send(b'Request')
    temperature = int.from_bytes(sock1.recv(4), 'big')
    humidity = int.from_bytes(sock1.recv(4), 'big')
    illuminance = int.from_bytes(sock1.recv(4), 'big')
    print(temperature, humidity, illuminance)
elif inputnumber == '2':
    sock2.send(b'Request')
    heartRate = int.from_bytes(sock2.recv(4), 'big')
    steps = int.from_bytes(sock2.recv(4), 'big')
    calories = int.from_bytes(sock2.recv(4), 'big')
    print(heartRate, steps, calories)
elif inputnumber == 'quit':
    sock1.send(b'quit')
    sock2.send(b'quit')
    sock1.close()
    sock2.close()

sock1.close()
sock2.close()