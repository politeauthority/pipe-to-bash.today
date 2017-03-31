import os
import logging

deployment = os.environ.get('PTBT_DEPLOYMENT', 'production')
_debug = False
_port = os.environ.get('PTBT_PORT', '80')

if deployment == 'dev':
    _debug = True
    _port = 8071

if __name__ == '__main__':
    from app import app
    logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)
    app.run(
        host="0.0.0.0",
        port=_port,
        debug=_debug
    )
