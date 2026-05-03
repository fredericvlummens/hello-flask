from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from ' + os.getenv('NAME', 'Howest') + '!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)