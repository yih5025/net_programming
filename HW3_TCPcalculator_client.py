from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4444))

while True:
    msg = input("Input your number and calculater: ")
    if msg == 'q':
        break
    s.send(msg.encode())

    

s.close()