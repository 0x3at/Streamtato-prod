import json
from app import create_app


def load_json_data(path):
    with open(path, 'r') as file:
        return json.load(file)


def add_media(media_data):
    media_data = sorted(media_data, key=lambda x: x['episode_number'])
    for item in media_data:
        media = Media(
            show_name=item.get('show_name'),
            episode_number=item.get('episode_number'),
            special=item.get('special', False),
            name=item['name'],
            title=item.get('title'),
            length=item['length'],
            year=item.get('year'),
            genre=item.get('genre'),
            rating=item.get('rating'),
            image_url=item['image_url'],
            video_url=item['video_url']
        )
        db.session.add(media)
    db.session.commit()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from app import db
        from app.models import Media
        path_list = ['app/static/courage/courage.json', "app/static/dragonball/dragonball.json",
                     "app/static/invaderzim/invaderzim.json"]
        for path in path_list:
            list_of_media = load_json_data(path)
            add_media(list_of_media)
            print(Media.query.all())

        for media in Media.query.all():
            if media.name == "DBsp1" or media.name == "DBsp2":
                db.session.delete(media)
                db.session.commit()
        print(media in Media.filter_by(show_name="DragonBall(1986)").all()
              if media.name == "DBsp1" or media.name == "DBsp2" else "not in db")
