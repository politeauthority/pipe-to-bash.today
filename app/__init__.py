import os
from flask import Flask
from flask import Response
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return Response(render_template('index.html'), 'text/html')


@app.route('/load/<script>')
def bash(script):
    """

    """
    base_bash_path = './bash'
    bash_path = os.path.join(base_bash_path, script + '.sh')
    if not os.path.exists(bash_path):
        bash_path = os.path.join(base_bash_path, '404.sh')
    phile = open(bash_path, 'r')
    data = phile.read()
    return Response(data, mimetype='text/text')
