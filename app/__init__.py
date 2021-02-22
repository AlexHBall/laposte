import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis
from rq import Queue

from app.config import config
from app.request.request import Request

db = SQLAlchemy()
request_handler = Request()
redis = redis.Redis()
queue = Queue(connection=redis)


def create_app():
    app = Flask(__name__)

    CORS(app, origins="*", supports_credentials=True)

    config_name = os.getenv("FLASK_CONFIG") or "default"
    app.config.from_object(config[config_name])

    from . import models
    from .weather import weather as weather_blueprint
    db.init_app(app)
    app.register_blueprint(weather_blueprint, url_prefix="/weather")
    return app
