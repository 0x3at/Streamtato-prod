from flask_login import LoginManager
from app.models import DatabaseInterface


def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = "/login"

    @login_manager.user_loader
    def load_user(user_id):
        return DatabaseInterface.get_user_by_id(user_id)

    login_manager.init_app(app)
    return app
