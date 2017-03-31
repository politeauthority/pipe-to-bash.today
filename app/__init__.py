import os
from flask import Flask
from flask import Response
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return Response(render_template('index.html'), 'text/html')


@app.route('/load/<script>')
@app.route('/l/<script>')
def bash(script):
    base_bash_path = './bash'
    bash_path = os.path.join(base_bash_path, script + '.sh')
    if not os.path.exists(bash_path):
        bash_path = os.path.join(base_bash_path, '404.sh')
    phile = open(bash_path, 'r')
    bash_data = phile.read()
    return Response(bash_data, mimetype='text/text')


@app.route('/gen/<script>')
def gen(script):
    """

    """
    # shit = request.headers['Host']  # prints "domain1.com"
    curl = "curl -sSL %s/l/%s | bash" % (request.headers['Host'], script)
    data = {
        'curl': curl
    }
    return __rend('generate_curl.html', data)


def __rend(template, data, _type="/text/html"):
    return Response(render_template(template, **data), _type)
