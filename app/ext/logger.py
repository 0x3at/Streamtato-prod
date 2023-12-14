import logging


def init_app(app):
    logging.basicConfig(
        level=logging.WARNING, format='%(asctime)s %(levelname)s %(name)s : %(message)s', filename='logs.log', filemode='w')
    return app
