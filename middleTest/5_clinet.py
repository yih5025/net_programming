import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 8888)

sock.connect(addr)
a = input('enter 1, 2, 3: ')

sock.send(a.encode())

msg = int.from_bytes(sock.recv(4), 'big')
humid = int.from_bytes(sock.recv(4), 'big')
lumi = int.from_bytes(sock.recv(4), 'big')


print('Temp=', msg, ', Humid=', humid,', Lumi=', lumi)


sock.close()