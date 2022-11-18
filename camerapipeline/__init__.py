from flask import Flask
from flask_injector import FlaskInjector
from flask_cors import CORS

from camerapipeline.core import routes

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

CORS(app)

routes.init_routes(app=app)

FlaskInjector(app=app)

if __name__ == "__main__":
    app.run()