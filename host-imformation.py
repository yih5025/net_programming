import socket

HOSTS = [
    'www.sch.ac.kr',
    'homepage.sch.ac.kr',
    'www.naver.com',
    'www.google.com',
]

for host in HOSTS:
    try: 
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg: 
        print('{} : {}'.format(host, msg))

