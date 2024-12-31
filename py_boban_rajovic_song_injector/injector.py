import random
from .models import Song, db

class BobanRajovicSongInjector:
    def __init__(self):
        self.songs = [
            {"title": "Usne Boje Vina", "url": "https://www.youtube.com/watch?v=cI1T5cQZ5qo"},
            {"title": "Teci Mi Kroz Vene", "url": "https://www.youtube.com/watch?v=TF9-gysFJxA"},
            {"title": "Padobran", "url": "https://www.youtube.com/watch?v=-X7oxcPSstw"},
            {"title": "Provokacija", "url": "https://www.youtube.com/watch?v=_Eg9QAxqT0s"},
            {"title": "Crna Lala", "url": "https://www.youtube.com/watch?v=CbijUv4hv3w"},
            {"title": "Kilometri Ljubavi", "url": "https://www.youtube.com/watch?v=_l4QgBHwJPk"},
            {"title": "Spartanac", "url": "https://www.youtube.com/watch?v=otNlZdUEF5c"},
            {"title": "Pomozite Mi Drugovi", "url": "https://www.youtube.com/watch?v=LdJErDkqimw"},
            {"title": "Flasa", "url": "https://www.youtube.com/watch?v=u0I62vFfrGw"},
            {"title": "Latice Od Ruza", "url": "https://www.youtube.com/watch?v=Hi_fVF658e4"},
            {"title": "Otkazi", "url": "https://www.youtube.com/watch?v=TbWQOi9J3P4"},
            {"title": "Interventna", "url": "https://www.youtube.com/watch?v=HEwT7CRTkAU"},
            {"title": "Generacijo", "url": "https://www.youtube.com/watch?v=hAo9gadmUX0"},
            {"title": "Baraba", "url": "https://www.youtube.com/watch?v=38G0_UW0PrM"},
            {"title": "Gromovi", "url": "https://www.youtube.com/watch?v=E5bTlEz480c"},
            {"title": "Bahato", "url": "https://www.youtube.com/watch?v=zj-qKeG5QiM"},
            {"title": "Lijepa zena", "url": "https://www.youtube.com/watch?v=X2kyMqWPaRc"},
            {"title": "Sve ti basta", "url": "https://www.youtube.com/watch?v=hIvOFdLaouE"},
            {"title": "Jedan je zivot", "url": "https://www.youtube.com/watch?v=haxdQ5GiCZQ"},
            {"title": "Pustite me", "url": "https://www.youtube.com/watch?v=7UZGqR13taw"},
            {"title": "Dijagnoza", "url": "https://www.youtube.com/watch?v=IMFtMghTat0"},
            {"title": "Oprosti mi", "url": "https://www.youtube.com/watch?v=WS5IygcCswA"},
            {"title": "Ne vjerujem", "url": "https://www.youtube.com/watch?v=qRGGYOp80KI"},
            {"title": "Kisa lije", "url": "https://www.youtube.com/watch?v=7F0a4VxrWpM"},
            {"title": "Princeza", "url": "https://www.youtube.com/watch?v=KyLIpY_Ljjc"},
            {"title": "Darovi", "url": "https://www.youtube.com/watch?v=2ksK_dgb1Jg"},
            {"title": "Nogu pred nogu", "url": "https://www.youtube.com/watch?v=2F9kvC-wp9E"},
            {"title": "Pijem da se otrijeznim od nje", "url": "https://www.youtube.com/watch?v=dNxgUjmg-s4"},
            {"title": "Kamen u cipeli", "url": "https://www.youtube.com/watch?v=_Ff07x1Qiis"},
            {"title": "Avion", "url": "https://www.youtube.com/watch?v=Y547Xgq2wPI"},
            {"title": "Ko na kraju dodje", "url": "https://www.youtube.com/watch?v=MUo3Y7yga_E"},
            {"title": "Gadura", "url": "https://www.youtube.com/watch?v=lc096SDyk1M"},
        ]

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

