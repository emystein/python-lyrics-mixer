import pytest
from songs.model import SongTitle
from lyrics_mixer.lyrics_mixer import LyricsMixer, ParagraphInterleaveLyricsMixStrategy, MixedLyrics
from wikia.lyrics_api_client import WikiaLyricsApiClient


@pytest.fixture
def mixer():
    return LyricsMixer(WikiaLyricsApiClient(), ParagraphInterleaveLyricsMixStrategy())


def test_mix_two_random_lyrics(mixer):
    mixed_lyrics = mixer.mix_two_random_lyrics()
    assert mixed_lyrics != MixedLyrics.empty()


def test_mix_random_lyrics_by_artists(mixer):
    mixed_lyrics = mixer.mix_random_lyrics_by_artists('U2', 'A-ha')
    assert mixed_lyrics != MixedLyrics.empty()


@pytest.mark.vcr()
def test_mix_two_specific_lyrics(mixer):
    title1 = SongTitle('U2', 'One')
    title2 = SongTitle('A-ha', 'Take on me')

    mixed_lyrics = mixer.mix_two_specific_lyrics(title1, title2)

    assert mixed_lyrics.title == str(title1) + ', ' + str(title2)
    assert mixed_lyrics.text != ''
