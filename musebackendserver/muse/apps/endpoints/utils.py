from .models import Song

def get_lyrics_from_ids_as_list(songIDs):
    SongsDict = Song.objects.in_bulk(songIDs)
    lyrics = []

    for song in SongsDict.values():
        lyrics.append(song.lyrics)
    return lyrics
