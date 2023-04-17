from flask import Flask, jsonify

import os
import platform
import subprocess

if not os.getenv('DWL_ENV'):
    path = os.path.dirname(os.path.abspath(__file__))

    if platform.system() == 'Linux':
        os.environ['DWL_ENV'] = os.path.join(path, 'cli', 'linux', 'bin', 'dw')
    else:
        os.environ['DWL_ENV'] = os.path.join(path, 'cli', 'windows', 'bin', 'dw.exe')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/dwl')
def dwl():
    cmd = "output application/json --- {'hello': 'world'}"
    result = subprocess.run(['dw', cmd], stdout=subprocess.PIPE)
    return jsonify({
        "hello": "Hello World", 
        "result": result.stdout.decode('utf-8'), 
        "cli": os.getenv('DWL_ENV')
    })

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True, port=8080)