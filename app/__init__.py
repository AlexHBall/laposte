import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.config import config
from app.request.request import Request

db = SQLAlchemy()
request_handler = Request()

def create_app():
    app = Flask(__name__)

    CORS(app, origins="*", supports_credentials=True)

    config_name = os.getenv("FLASK_CONFIG") or "default"
    app.config.from_object(config[config_name])



    from . import models
    from .v1 import v1 as v1_blueprint
    db.init_app(app)
    app.register_blueprint(v1_blueprint, url_prefix="/v1")
    return app