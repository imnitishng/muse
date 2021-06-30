from .models import Song


def is_duplicate_song_serializer_error(errors):
    spotify_id_error = errors.get('spotify_id', None)
    if len(errors) == 1 and spotify_id_error and len(spotify_id_error) == 1:
        if str(spotify_id_error[0]) == 'song with this spotify id already exists.':
            return True
    return False
    
def remove_invalid_data_from_raw_list(serializer, data_list):
    '''
    Takes a list serializer object (many=True) and a list as an input and
    removes invalid data based on the errors from `serializer.errors`
    '''
    indexes_to_delete = []

    for i, error in enumerate(serializer.errors):
        if error:
            indexes_to_delete.append(i)

    valid_data = [data for i, data in enumerate(data_list) if i not in indexes_to_delete]
    return valid_data

def ignore_invalid_and_save_list(data_list, serializer):
    '''
    Ignores invalid serialized entries and saves only valid data from
    a list of Model objects using serializers, used only for `many = True`.
    
    Returns:
        A list saved Django object models 
    '''
    serialized_data = serializer(data=data_list, many=True)

    if serialized_data.is_valid():
        saved_data = serialized_data.save()
    else:
        valid_data_list = remove_invalid_data_from_raw_list(serialized_data, data_list)
        serialized_data = serializer(data=valid_data_list, many=True)
        if serialized_data.is_valid(raise_exception=True):
            saved_data = serialized_data.save()
    return saved_data

def get_lyrics_from_ids_as_list(songIDs):
    SongsDict = Song.objects.in_bulk(songIDs)
    lyrics = []

    for song in SongsDict.values():
        lyrics.append(song.lyrics)
    return lyrics
