from socket import *

BUFSIZE = 1024
port = 3500

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("send [mboxID] message or received [mboxID] or quit: ")

    c_sock.sendto(msg.encode(), ('localhost', port))

    data, addr = c_sock.recvfrom(BUFSIZE)

    print(data.decode())
