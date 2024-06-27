from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults

# Define the messages you want to print and serve
messages = [
    'hjlh',
    'dhgkdjhg',
    'hello world',
    'Nidhesh'
]

def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    # Set the response headers
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    response_body = '\n'.join(messages).encode('utf-8')
    
    # Print each message
    for message in messages:
        print(message)

    return [response_body]

if __name__ == '__main__':
    PORT = 8000
    httpd = make_server('', PORT, simple_app)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
