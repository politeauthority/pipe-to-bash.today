import os

deployment = os.environ.get('PTBT_DEPLOYMENT', 'production')

_debug = False
_port = 80
if deployment == 'dev':
    _debug = True
    _port = 8071

if __name__ == '__main__':
    from app import app
    app.run(
        host="0.0.0.0",
        port=_port,
        debug=_debug
    )
