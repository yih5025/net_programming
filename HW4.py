import socket

# MIME 타입 설정
mimetypes = {
    'html': 'text/html',
    'png': 'image/png',
    'ico': 'image/x-icon'
}

# 웹 서버 소켓 생성
host = 'localhost'
port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

while True:
    # 클라이언트 연결 대기
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # HTTP Request 첫 번째 라인 읽기
    request = client_socket.recv(1024).decode()
    request_line = request.split('\r\n')[0]

    # 요청 라인 파싱
    method, filename, _ = request_line.split()
    filename = filename[1:]  # '/' 제거

    # 요청에 따른 파일 및 MIME 타입 설정
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
        client_socket.sendall(response)
    except FileNotFoundError:
        # 파일이 존재하지 않는 경우 404 Not Found 응답 전송
        response_header = 'HTTP/1.1 404 Not Found\r\n'
        response_header += '\r\n'
        response_body = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        response = response_header.encode() + response_body
        client_socket.sendall(response)

    # 클라이언트 소켓 닫기
    client_socket.close()

# 서버 소켓 닫기
server_socket.close()
