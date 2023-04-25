import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Enter the massage: ")
    if msg == 'q':
        break

    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFSIZE)
    print('Server says: ', data.decode())

sock.close()