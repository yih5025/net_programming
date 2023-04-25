import socket

port = int(input("port No: "))
address = ("localhost", port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True : 
    msg = input("Message to send: ")
    try :
        bytesSent = s.send(msg.encode())
    except: 
        print(print('connection closed'))
        break
    else:
        print("{} bytes send" .format(bytesSent))

    try: 
        data = s.recv(BUFSIZE)
    except: 
        print('connection closed')
        break
    else: 
        if not data:
            break
        print("Received message: %s" % data.decode())

s.close()