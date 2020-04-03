import pytest
from unittest.mock import Mock
from songs.tests.fixtures.songs import song1, song2
from lyrics_mixer.twitter.reply_composer import MixLyricsReplyComposer
from lyrics_mixer.mixed_lyrics import MixedLyrics
from twitter.tests.model import TweetForTest


parsed_song_titles = Mock()

reply_composer = MixLyricsReplyComposer(lyrics_mixer=Mock())


def test_reply(song1, song2):
    tweet = TweetForTest('emenendez', 'text')

    expected_mixed_lyrics = MixedLyrics(song1, song2, [], [])

    parsed_song_titles.mix.return_value = expected_mixed_lyrics

    result = reply_composer.write_reply(tweet, parsed_song_titles)

    assert result == f"@{tweet.user.name} {expected_mixed_lyrics}"


def test_exception_on_mix():
    parsed_song_titles.mix.side_effect = RuntimeError('Error mixing songs')

    with pytest.raises(Exception):
        reply_composer.write_reply("some tweet", parsed_song_titles)