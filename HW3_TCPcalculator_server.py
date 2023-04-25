from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(2)

print("Please waiting....")

while True:
    client, addr = s.accept()
    print("connection from", addr)
    while True:
        data = client.recv(1024)
        print(data[0], data[1], data[2], data[3])

        '''
        try:
            data_list = re.split(r'[+\-*/]', data)
        except:
            client.send(b'Try again')
        else:
        '''

            

s.close()