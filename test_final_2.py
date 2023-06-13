import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

class ImageServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # 웹 페이지에 이미지 출력
            self.wfile.write(b'<html><body><img src="./iot.png"></body></html>')
        elif self.path == '/iot.png':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            # 이미지 파일 전송
            with open('./iot.png', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

host = 'localhost'
port = 8888
server_address = (host, port)

def run_server():
    httpd = HTTPServer(server_address, ImageServer)
    print(f'Starting web server on {host}:{port}')
    httpd.serve_forever()

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
