import os, pathlib, json, re

class LyricsEncoderModel:
    
    def __init__(self):
        pass

    def pre_processing(self, JSON_data):
        songs, lyrics = JSON_data.get('song', None), JSON_data.get('lyrics', None)

        self.processed_lyrics = remove_duplicate_lines(lyrics)
        return {
            "songs": songs, 
            "lyrics": self.processed_lyrics,
            "status": "OK"
        }


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
    """
    for i in range(len(lyrics)):
        lyrics[i] = re.sub('\[.*?\]\n', '', lyrics[i])
    return lyrics