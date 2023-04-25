import socket

ip = '220.69.189.125'
port = 443

hostname = socket.getfqdn(ip)
print(hostname)

hport = socket.getservbyport(port)
print(hport)


print('{}://{}'.format(hport, hostname))

byte = socket.inet_aton(ip)
print(byte)