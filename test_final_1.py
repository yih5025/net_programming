from http.server import SimpleHTTPRequestHandler, HTTPServer

# 웹 서버 클래스 정의
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

# 서버 설정
host = 'localhost'
port = 8888
server_address = (host, port)

try:
    # 서버 실행
    httpd = HTTPServer(server_address, ImageServer)
    print(f'Starting web server on {host}:{port}')
    httpd.serve_forever()
except KeyboardInterrupt:
    # 서버 종료 시 Ctrl+C 입력 처리
    httpd.server_close()
    print('Stopping web server')
