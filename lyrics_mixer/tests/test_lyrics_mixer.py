import pytest
from lyrics_mixer.tests.fixtures.mocks import lyrics_library_mock
import songs.tests.song_factory
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.song_titles_parser import ParsedArtists
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMix, ParagraphInterleaveLyricsMix, MixedLyrics, EmptyMixedLyrics


lyrics_mix_strategy = LineInterleaveLyricsMix()


def test_two_random_songs_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_random_songs.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_two_random_lyrics()

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_random_songs_by_artists_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_random_lyrics_by_artists(song1.title.artist, song2.title.artist)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_two_specific_songs_mixer(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_songs.return_value = [song1, song2]

	mixed_lyrics = mixer.mix_two_specific_lyrics(song1.title, song2.title)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_error_on_lyrics_download(lyrics_library_mock, song1, song2):
	lyrics_library_mock.get_random_songs.side_effect = RuntimeError('Cannot download lyrics')

	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	with pytest.raises(Exception):
		mixer.mix_two_random_lyrics()


def test_mix_parsed_song_titles(lyrics_library_mock, song1, song2):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)

	lyrics_library_mock.get_random_songs_by_artists.return_value = [song1, song2]

	parsed_song_titles = ParsedArtists(['Led Zeppelin', 'Steppenwolf'])

	mixed_lyrics = mixer.mix_parsed_song_titles(parsed_song_titles)

	assert mixed_lyrics == lyrics_mix_strategy.mix(song1, song2)


def test_exception_on_mix_parsed_song_titles(lyrics_library_mock):
	mixer = LyricsMixer(lyrics_library_mock, lyrics_mix_strategy)
	
	lyrics_library_mock.get_random_songs_by_artists.side_effect = RuntimeError('Error mixing songs')
	
	parsed_song_titles = ParsedArtists(['Led Zeppelin', 'Steppenwolf'])

	mixed_lyrics = mixer.mix_parsed_song_titles(parsed_song_titles)

	assert mixed_lyrics == EmptyMixedLyrics()


def test_mixed_lyrics(song1, song2):
	lyrics_editor = ParagraphInterleaveLyricsMix()
	expected = lyrics_editor.mix(song1, song2)

	mixed_lyrics = MixedLyrics(song1, song2, [], expected.paragraphs)

	assert mixed_lyrics.title == str(song1.title) + ', ' + str(song2.title)
	assert mixed_lyrics.text == '\n\n'.join(expected.paragraphs)


