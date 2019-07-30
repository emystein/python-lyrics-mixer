import pytest
from app.random_lyrics_downloader import RandomLyricsDownloader
from app.song import SongTitle
from wikia.random_song_url_parser import WikiaRandomSongUrlParser
from wikia.lyrics_api_adapter import WikiaLyricsApiClient


@pytest.fixture
def downloader():
    return RandomLyricsDownloader(WikiaRandomSongUrlParser(), WikiaLyricsApiClient())


def test_get_random_lyrics_from_wikia(downloader):
    song = downloader.get_random()
    assert song.title != SongTitle('', '')
    assert song.lyrics != ''


def test_get_random_lyrics_by_artist_from_wikia(downloader):
    song = downloader.get_random_by_artist('Led Zeppelin')
    assert song.title.artist == 'Led Zeppelin'
    assert song.title.title != ''
    assert song.lyrics != ''
