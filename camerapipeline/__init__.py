from flask import Flask
from flask_injector import FlaskInjector
from flask_cors import CORS

from camerapipeline.core import routes

app = Flask(__name__, instance_relative_config=True)

CORS(app)

routes.init_routes(app=app)

FlaskInjector(app=app)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()