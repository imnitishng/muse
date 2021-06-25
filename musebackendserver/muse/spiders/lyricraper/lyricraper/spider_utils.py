import os

from apps.endpoints.models import Song, SongQueryObject, QueryStatus

def defaulters_to_file(artist, song):
    """
    Save the songs not found in Genius to a to_mxm.txt
    """
    
    with open('to_mxm.txt', 'a+') as f:
        print(f'{artist} - {song}', file=f) 

def getSongIDsToScrape1(query):
    '''
    Remove the songs which do not need lyrics scraping
    (Lyrics already present) for 1st spider (Genius)
    '''

    songs_requested = query.songids_to_process.split(',')
    if songs_requested:
        QueriedSongsDict = Song.objects.in_bulk(songs_requested)
        QueriedSongsDictFiltered = dict()
        for pk, song in QueriedSongsDict.items():
            if not song.lyrics:
                QueriedSongsDictFiltered[pk] = song
        
        songs_to_scrape = str(list(QueriedSongsDictFiltered.keys()))[1:-1]
        query.songids_to_process = songs_to_scrape
        query.save()
        return 1
    else:
        return None
