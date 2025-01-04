from flask import Flask

from py_boban_rajovic_song_injector.models import db
from py_boban_rajovic_song_injector import BobanRajovicSongInjector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        injector = BobanRajovicSongInjector()
        injector.inject_songs(10)
        print("Unique songs injected into the database.")
