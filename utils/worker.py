import re

from lyricsgenius import Genius

from config import config


genius = Genius(config['api']['token'])


def lyrics_getter(artist, song):
    data = genius.search_song(song, artist)
    if data is not None:
        return re.sub(r'[0-9Embed]+$', "", data.lyrics.replace("You might also like",'\n'))
    return "Error"
