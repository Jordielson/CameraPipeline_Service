import os
from flask import Flask
from flask_injector import FlaskInjector
from flask_cors import CORS

from app.core import routes

app = Flask(__name__)

CORS(app)

routes.init_routes(app=app)

FlaskInjector(app=app)

if __name__ == "__main__":
    app.run()