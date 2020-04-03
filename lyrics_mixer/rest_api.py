from flask import Flask, escape
from datetime import datetime
from lyrics_mixer.lyrics_mixer import LyricsMixer
from songs.model import SongTitle


def configure_views(app):
	@app.route('/')
	def home():
		return f'{datetime.now()}: OK\n'


	@app.route('/mix/random')
	def mix_two_random_lyrics(lyrics_mixer: LyricsMixer):
		mixed = lyrics_mixer.mix_two_random_lyrics()
		return f'{escape(str(mixed))}'


	@app.route('/mix/artists/<artist1>/<artist2>')
	def mix_random_lyrics_by_artists(lyrics_mixer: LyricsMixer, artist1, artist2):
		mixed = lyrics_mixer.mix_random_lyrics_by_artists(artist1, artist2)
		return f'{escape(str(mixed))}'


	@app.route('/mix/songs/<artist1>/<title1>/<artist2>/<title2>')
	def mix_two_specific_lyrics(lyrics_mixer: LyricsMixer, artist1, title1, artist2, title2):
		mixed = lyrics_mixer.mix_two_specific_lyrics(
			SongTitle(artist1, title1), SongTitle(artist2, title2))
		return f'{escape(str(mixed))}'
