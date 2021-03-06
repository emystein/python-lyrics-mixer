import pytest
from lyrics_mixer.lyrics_mixer import LineInterleaveLyricsMix
from songs.model import Song, Lyrics


@pytest.fixture
def lyrics_editor():
    return LineInterleaveLyricsMix()


def test_mix_with_same_number_of_lines(lyrics_editor):
    song1 = Song('artist1', 'title1',
                 Lyrics('lyrics 1 line 2\nlyrics 1 line 2\n\nlyrics 1 line 3'))
    song2 = Song('artist2', 'title2',
                 Lyrics('lyrics 2 line 2\nlyrics 2 line 2\n\nlyrics 2 line 3'))
    mixed_lyrics = lyrics_editor.mix(song1, song2)
    assert mixed_lyrics.lines == [
        'lyrics 1 line 2', 'lyrics 2 line 2', 'lyrics 1 line 2', 'lyrics 2 line 2', '', '', 'lyrics 1 line 3', 'lyrics 2 line 3']


def test_mix_with_first_lyrics_with_2_lines_and_second_lyrics_with_1_line(lyrics_editor):
    song1 = Song('artist1', 'title1',
                 Lyrics('lyrics 1 line 2\nlyrics 1 line 2'))
    song2 = Song('artist2', 'title2', Lyrics('lyrics 2 line 2'))
    mixed_lyrics = lyrics_editor.mix(song1, song2)
    assert mixed_lyrics.lines == ['lyrics 1 line 2', 'lyrics 2 line 2']


def test_mix_with_first_lyrics_with_1_line_and_second_lyrics_with_2_lines(lyrics_editor):
    song1 = Song('artist1', 'title1', Lyrics('lyrics 1 line 2'))
    song2 = Song('artist2', 'title2',
                 Lyrics('lyrics 2 line 2\nlyrics 2 line 2'))
    mixed_lyrics = lyrics_editor.mix(song1, song2)
    assert mixed_lyrics.lines == ['lyrics 1 line 2', 'lyrics 2 line 2']


def test_mix_with_first_paragraph_containing_one_line_and_second_paragraph_containing_two_lines(lyrics_editor):
    song1 = Song('artist1', 'title1',
                 Lyrics('lyrics 1 line 2\nlyrics 1 line 2\n\nlyrics 1 line 3'))
    song2 = Song('artist2', 'title2',
                 Lyrics('lyrics 2 line 2\nlyrics 2 line 2\n\nlyrics 2 line 3'))
    mixed_lyrics = lyrics_editor.mix(song1, song2)
    assert mixed_lyrics.lines == ['lyrics 1 line 2', 'lyrics 2 line 2', 'lyrics 1 line 2',
                                  'lyrics 2 line 2', '', '', 'lyrics 1 line 3', 'lyrics 2 line 3']
    assert mixed_lyrics.paragraphs == [
        'lyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 2\nlyrics 2 line 2', 'lyrics 1 line 3\nlyrics 2 line 3']


def test_mix_with_first_paragraph_containing_two_lines_and_second_paragraph_containing_one_line(lyrics_editor):
    song1 = Song('artist1', 'title1',
                 Lyrics('lyrics 1 line 2\n\nlyrics 1 line 2\nlyrics 1 line 3'))
    song2 = Song('artist2', 'title2',
                 Lyrics('lyrics 2 line 2\n\nlyrics 2 line 2\nlyrics 2 line 3'))
    mixed_lyrics = lyrics_editor.mix(song1, song2)
    assert mixed_lyrics.lines == ['lyrics 1 line 2', 'lyrics 2 line 2', '', '',
                                  'lyrics 1 line 2', 'lyrics 2 line 2', 'lyrics 1 line 3', 'lyrics 2 line 3']
    assert mixed_lyrics.paragraphs == ['lyrics 1 line 2\nlyrics 2 line 2',
                                       'lyrics 1 line 2\nlyrics 2 line 2\nlyrics 1 line 3\nlyrics 2 line 3']
