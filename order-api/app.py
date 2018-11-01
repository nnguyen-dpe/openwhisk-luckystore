import os

from flask import Flask
from apis.api import api
from apis.routes import ns as order_ns

app = Flask(__name__)
api.add_namespace(order_ns, '/api/v1')
api.init_app(app)

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)
