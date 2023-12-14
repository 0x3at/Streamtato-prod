from flask import Flask
from .config import Config
from .ext import database
from .ext import blueprint
from .ext import login
from .ext import logger


db = database.DB


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)
    blueprint.init_app(app)
    login.init_app(app)
    logger.init_app(app)
    app.logger.info('App created')

    return app
