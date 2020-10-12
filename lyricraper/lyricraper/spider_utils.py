import os

def defaulters_to_file(artist, song):
    """Save the songs not found in Genius to a to_mxm.txt"""
    
    with open('to_mxm.txt', 'a+') as f:        
        print(f'{artist} - {song}', file=f) 