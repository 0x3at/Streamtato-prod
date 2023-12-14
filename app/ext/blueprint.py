from ..blueprints import (
    index_bp,
    login_bp,
    logout_bp,
    register_bp,
    shows_bp,
    watch_bp,
    stream_bp
)


def init_app(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(shows_bp)
    app.register_blueprint(watch_bp)
    app.register_blueprint(stream_bp)
    return app
