from ..ext.database import DB as db


class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(150), nullable=True)
    episode_number = db.Column(db.Integer, nullable=True)
    special = db.Column(db.Boolean, nullable=True)
    name = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(150))
    length = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(150), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(500), nullable=False)
    video_url = db.Column(db.String(500), nullable=False)
