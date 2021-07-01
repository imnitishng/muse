from django.db.models import Q

from apps.endpoints.models import Song


def defaulters_to_file(artist, song):
    """
    Save the songs not found in Genius to a to_mxm.txt
    """    
    with open('to_mxm.txt', 'a+') as f:
        print(f'{artist} - {song}', file=f) 

def getSongIDsToScrape1(all_song_ids):
    '''
    Select the songs from the database that do not have lyrics 
    stored or need a second turn at scraping lyrics since the 
    spider failed to scrape lyrics at an earlier point in time.
    '''
    songs_to_scrape = Song.objects.filter(
        pk__in=all_song_ids
    ).filter(
        Q(lyrics=None) | Q(lyrics__iexact='scraping_failed')
    ).values_list(
        'id', flat=True
    )

    return list(map(lambda x: x.hex, songs_to_scrape))