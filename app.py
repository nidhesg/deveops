import http.server
import socketserver

# Define the messages you want to print and serve
messages = [
    'hjlh',
    'dhgkdjhg',
    'hello world',
    'Nidhesh'
]

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Print each message and send it as the HTTP response
        for message in messages:
            print(message)
            self.wfile.write(message.encode('utf-8') + b'\n')

if __name__ == '__main__':
    PORT = 8000
    handler = MyHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Server started on port {PORT}")
        httpd.serve_forever()
