from socket import *

BUFSIZE = 1024
port = 3500

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

mboxes = dict()

while True:
    data, addr = s_sock.recvfrom(BUFSIZE)
    ddata = data.decode()
    
    if ddata.startswith('send') :
        parts = ddata.split()
        if len(parts) < 3 :    
            s_sock.sendto('형식에 맞게 다시 입력해주세요.'.encode(), addr)
            continue
        else: #맞게 들어왔을때
            print(parts)
            mboxID = parts[1]
            text = " ".join(parts[2:])
            if mboxID not in mboxes:
                mboxes[mboxID] = []
            mboxes[mboxID].append(text)
            print(mboxes)
            s_sock.sendto("OK".encode(), addr)
    elif ddata.startswith('received'):
        parts = ddata.split()
        print(parts)
        if len(parts) < 2:
            s_sock.sendto('형식에 맞게 다시 입력해주세요.'.encode(), addr)
            continue
        else: 
            mboxID = parts[1]
            if mboxID not in mboxes or len(mboxes[mboxID]) == 0:
                s_sock.sendto("No messages".encode(), addr)
                continue
            else: #다 있어 정상일때
                recivedMsg = mboxes[mboxID][0]
                print('sendto', recivedMsg)
                s_sock.sendto(recivedMsg.encode(), addr)
                mboxes[mboxID].pop(0)      
            print(mboxes)
    elif ddata == 'quit':
        print('quit')
        break

s_sock.close()
