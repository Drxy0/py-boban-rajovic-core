import random
import random
from .models import Song, db, songs

class BobanRajovicSongInjector:
    def __init__(self):
        self.songs = songs

    def inject_songs(self, number_of_songs=10):
        """Inject a specified number of random songs into the database."""
        # Generate a list of random songs
        random_songs = [self.get_random_song() for _ in range(number_of_songs)]
        
        for title, url in random_songs:
            new_song = Song(title=title, url=url)
            db.session.add(new_song)
        
        db.session.commit()

    def inject_songs_no_repeat(self, number_of_songs=10):
        """Inject a specified number of random songs into the database without repetition."""
        if number_of_songs > len(self.songs):
            raise ValueError("Requested number of songs exceeds available songs.")

        # Shuffle the songs and select the first `number_of_songs` songs
        selected_songs = random.sample(self.songs, number_of_songs)
        
        for song in selected_songs:
            new_song = Song(title=song["title"], url=song["url"])
            db.session.add(new_song)
        
        db.session.commit()

    def get_random_song(self):
        return random.choice(self.songs) if self.songs else ("Unknown Title", "Unknown URL")

