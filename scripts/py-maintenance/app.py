from flask import Flask
from flask_restful import Api
from rest_layer.resources import routes
import os
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

app = Flask(__name__)
api = Api(app)
routes.initialize_routes(api)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
