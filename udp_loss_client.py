from socket import *

BUFSIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

for i in range(10) :
    time = 0.1
    data = "Hello, IoT"
    while True:
        sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack' .format(i, time))
        sock.settimeout(time)

        try:
            data = sock.recv(BUFSIZE)
        except timeout:
            time *= 2
            if time > 2.0 :
                print("time out!!!")
                break
        else:
            print("Recived ", data.decode())
            break