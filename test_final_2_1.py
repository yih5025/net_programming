import threading
import socket
import os

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode()
    # HTTP 응답 메시지 생성
    status_line = "HTTP/1.1 200 OK\r\n"
    content_type_header = "Content-Type: image/png\r\n"
    end_of_headers = "\r\n"

    image_path = "./iot.png"

    if not os.path.exists(image_path):
        status_line = "HTTP/1.1 404 Not Found\r\n"
        content_type_header = "Content-Type: text/html\r\n"
        response_body = "404 Not Found"
    else:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        response_body = image_data

    response = status_line + content_type_header + end_of_headers + response_body

    # HTTP 응답 전송
    client_socket.sendall(response.encode())
    client_socket.close()

def run_server():
    host = 'localhost'
    port = 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f'Starting web server on {host}:{port}')

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()

try:
# 서버 스레드 실행
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    while True:
        if input('Press q to quit: ') == 'q':
            server_thread.join()
            break
except KeyboardInterrupt:
# Ctrl+C 입력 시 서버 스레드 정리
    server_thread.join()
    print('Stopping web server')