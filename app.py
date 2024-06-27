from flask import Flask  # Replace with your framework/library if not using Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define other routes and application logic as needed

# WSGI entry point
application = app  # This is the WSGI callable that Gunicorn expects
