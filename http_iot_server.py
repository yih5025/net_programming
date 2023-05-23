from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()
    def do_POST(self):
        self.route()

    def route(self):
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path

        if real_path == '/':
            self.send_html()
        elif real_path == '/button':
            self.proc_query()
        elif real_path == '/form_get':
            self.proc_query()
        elif real_path == '/form_post':
            self.proc_form_post()
        else:
            self.response(404, '<h1>Not Found</h1>')
    
    def send_html(self):
        