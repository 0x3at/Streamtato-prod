from flask import current_app

from .media import Media
from .user import User


class DatabaseInterface:
    @staticmethod
    def get_user_by_id(id):
        current_app.logger.info(f"Database was queried for user {id}")
        return User.query.filter_by(id=id).first()

    @staticmethod
    def get_user_by_username(username):
        current_app.logger.info(f"Database was queried for user {username}")
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        current_app.logger.info(f"Database was queried for user {email}")
        return User.query.filter_by(email=email).first()

    @staticmethod
    def add_new_user(username, email, password):
        current_app.logger.warning(
            f"Database was modfied to add user {username}")
        from app import db
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_media():
        current_app.logger.info(f"Database was queried for all media")
        return Media.query.all()

    @staticmethod
    def get_media_by_id(id):
        current_app.logger.info(f"Database was queried for media {id}")
        return Media.query.filter_by(id=id).first()

    @staticmethod
    def get_all_show_names():
        current_app.logger.info(f"Database was queried for all show names")
        return set([media.show_name for media in Media.query.all() if media.show_name])

    @staticmethod
    def get_sorted_episodes_by_show(show):
        current_app.logger.info(
            f"Database was queried for all episodes of show {show}")
        return sorted([media for media in Media.query.filter_by(show_name=show).all() if not media.special],
                      key=lambda x: x.episode_number)
