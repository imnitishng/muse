import os, pathlib, json, re, requests

from django.conf import settings

FLASK_HOST = settings.FLASK_HOST

class UniversalSentenceEncoder:
    
    def __init__(self):
        self.processed_lyrics = None

    def pre_processing(self, lyrics):
        self.processed_lyrics = remove_duplicate_lines(lyrics)
        return self.processed_lyrics

    def get_model_results(self, payload):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = FLASK_HOST + '/embeddings'

        r = requests.post(
            url=url,
            json=payload,
            headers=headers,
            timeout=30
        )
        #TODO: What happens if this times out? Add Code
        return r


def remove_duplicate_lines(data):
    """
    Remove all the duplicate lines in a song lyrics
    """
    sanitized_lyrics_list = sanitize_tags(data)
    
    final_lyrics_list = []

    for lyric in sanitized_lyrics_list:
        hashmap = {}
        one_liners = lyric.split('\n')
        for val in one_liners:
            hashed = hash(val)
            hashmap[hashed] = val            
        final_lyrics = ' '.join(list(hashmap.values()))
        final_lyrics_list.append(final_lyrics)
    return final_lyrics_list


def sanitize_tags(lyrics):
    """
    Remove the [Chorus] tags from Genius lyrics
    Nothing happens if lyrics are not from Genius
    """
    for i in range(len(lyrics)):
        if lyrics[i]:
            lyrics[i] = re.sub('\[.*?\]\n', '', lyrics[i])
        else:
            lyrics[i] = 'NULL'
    return lyrics

