import logging
import schedule
import time
import os
from urllib.parse import urlparse, uses_netloc
from peewee import *
import psycopg2
from lyrics_mixer.lyrics_mixer import LyricsMixer, LineInterleaveLyricsMixStrategy
from lyrics_mixer.song_titles_parser import SongTitlesSplitter, SongTitlesParser
import jobs
import twitter.twitter
from twitter.persistence import StreamCursor
from twitter.twitter import TwitterApi
from lyrics_mixer.lyrics_data_source import LyricsDataSource

logging.basicConfig(level=logging.INFO)

if 'DATABASE_URL' in os.environ:
    uses_netloc.append('postgres')
    url = urlparse(os.environ["DATABASE_URL"])
    database = PostgresqlDatabase(
        database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
else:
    database = SqliteDatabase(':memory:')

database.bind([StreamCursor])

api = twitter.twitter.create_tweepy_api()

twitter_api = TwitterApi(api)

lyrics_mixer = LyricsMixer(LyricsDataSource(), LineInterleaveLyricsMixStrategy())

schedule.every().minute.do(jobs.reply_to_mentions, twitter_api=twitter_api,
                           tweet_parser=SongTitlesParser(SongTitlesSplitter()),
                           lyrics_mixer=lyrics_mixer)

schedule.every(4).hours.do(jobs.tweet_random_lyrics,
                           twitter_api=twitter_api,
                           lyrics_mixer=lyrics_mixer).run()


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()