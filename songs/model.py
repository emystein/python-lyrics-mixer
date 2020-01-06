class Song:
    def __init__(self, artist, title, lyrics_text):
        self.title, self.lyrics = SongTitle(artist, title), Lyrics(lyrics_text)


class NullSong:
    def __init__(self):
        self.title, self.lyrics = SongTitle('', ''), Lyrics('')
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.lyrics == other.lyrics)

class SongTitle:
    def __init__(self, artist, title):
        self.artist, self.title = artist.strip(), title.strip()

    def __eq__(self, other):
        return (self.artist == other.artist) and (self.title == other.title)

    def __str__(self):
        return self.artist + ' - ' + self.title


class Lyrics:
    def __init__(self, text):
        self.text = text

    def lines(self):
        return self.text.split('\n')

    def paragraphs(self):
        return self.text.split('\n\n')

    def __str__(self):
        return self.text

    def __eq__(self, other):
        return (self.text == other.text)