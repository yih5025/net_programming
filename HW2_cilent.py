import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = "ILHan Yu"
addr = ('localhost', 9002)

sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send(name.encode())


number = int.from_bytes(sock.recv(8), 'big')
print(number)
sock.close()