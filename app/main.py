import socket
import os
import uuid
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

@app.route('/')
def hello():
    return 'Hello,Max! This is your first application on Python!'


@app.route('/hostname')
def hostname() -> str:
    hostname=socket.gethostname()
    return hostname

@app.route('/author')
def author() -> str:
    return os.environ['AUTHOR']

# @app.route('/id')
# def id() -> str:
#     return str(uuid.uuid4())

@app.route('/id')
def id() -> str:
    return os.environ['POD_ID']

@app.route('/healthcheck')
def hc() -> str:
    return 'Everything is fine!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)