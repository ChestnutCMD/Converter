from flask import Flask
from flask_restx import Api

from view import api_ns

app = Flask(__name__)
api = Api(app)
api.add_namespace(api_ns)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
