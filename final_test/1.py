import selectors
import socket

sel = selectors.DefaultSelector()

mimetypes = {
    'html': 'text/html',
    'png': 'image/png',
    'ico': 'image/x-icon'
}

def accept(sock, mask):
    conn, addr = sock.accept()
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    request = conn.recv(1024).decode()
    print('request:', request)
    request_line = request.split('\r\n')[0]

    method, filename, _ = request_line.split()
    filename = filename[1:]
    print('filename: ', filename)

    if filename == '':
        filename = 'index.html'
    file_extension = filename.split('.')[-1].lower()
    mimetype = mimetypes.get(file_extension, 'text/html')

    try:
        # 파일 열기
        if file_extension == 'html':
            file = open(filename, 'r', encoding='utf-8')
        else:
            file = open(filename, 'rb')
        data = file.read()
        file.close()

        # HTTP Response 생성 및 전송
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Type: ' + mimetype + '\r\n'
        response_header += '\r\n'
        response_body = data
        response = response_header.encode() + response_body
        conn.sendall(response)

    except FileNotFoundError:
        # 파일이 존재하지 않는 경우 404 Not Found 응답 전송
        response_header = 'HTTP/1.1 404 Not Found\r\n'
        response_header += '\r\n'
        response_body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        response = response_header.encode() + response_body.encode()
        conn.sendall(response)
    

host = 'localhost'
port = 8080
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind((host, port))
s_sock.listen(5)

sel.register(s_sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
