from flask import Flask

from .ext import database
from .ext import blueprint
from .ext import login
from .ext import logger


db = database.DB


def create_app(settings):
    app = Flask(__name__)
    app.config.from_object(settings)
    database.init_app(app)
    blueprint.init_app(app)
    login.init_app(app)
    logger.init_app(app)
    app.logger.info('App created')

    return app
