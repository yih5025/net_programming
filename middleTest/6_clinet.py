from socket import *
import time

BUFSIZE = 1024
port = 7777

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

while True:
    ping = 'ping'

    sock.send(ping.encode())

    atime = time.time()

    data, addr = sock.recvfrom(BUFSIZE)
    print(data.decode())

    btime = time.time()

    RTT = btime - atime

    if data.decode() == 'pong':
        print('Success (RTT: ', RTT, ')')
    else:
        print('Fail')
    
    break

sock.close()