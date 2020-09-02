import pytest
import songs.tests.song_title_factory

@pytest.fixture
def song_titles():
    factory = songs.tests.song_title_factory
    return [factory.create_stairway_to_heaven(), factory.create_born_to_be_wild()]


@pytest.fixture
def song_title1():
    return songs.tests.song_title_factory.create_stairway_to_heaven()


@pytest.fixture
def song_title2():
    return songs.tests.song_title_factory.create_born_to_be_wild()