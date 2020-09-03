import pytest
import lyricwikia
from wikia.lyrics_api_client import Artist
from songs.model import SongTitle, NullSong, Song, Lyrics, EmptyLyrics
from songs.tests.fixtures.song_titles import song_titles, song_title1, song_title2

def test_get_all_songs_by_artist():
    assert len(Artist.named('Led Zeppelin').all_songs()) == 156


def test_get_random_song_by_artist():
    song = Artist.named('Led Zeppelin').random_song()

    assert song.artist == 'Led Zeppelin'
    assert song.title != ''
    assert song.has_lyrics()


def test_lyrics_not_found():
    assert Artist.named('Menéndez').random_song() == NullSong()