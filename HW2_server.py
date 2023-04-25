import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
number = 20191539

s.bind(('localhost', 9002))

s.listen(2)

while True:
    client, addr = s.accept()
    print('Connect from', addr)
    client.send(b'Hello '+ addr[0].encode())

    msg = client.recv(1024)
    print(msg.decode())

    numberToBytes = number.to_bytes(8, 'big')
    client.send(numberToBytes)
    
    client.close()