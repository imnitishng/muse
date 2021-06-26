# Generated by Django 3.1.2 on 2021-06-25 06:19

from django.db import migrations


def populateRecommendations(apps, schema_editor):
    Song = apps.get_model('endpoints', 'Song')
    SongQueryObject = apps.get_model('endpoints', 'SongQueryObject')
    UserTrackSelection = apps.get_model('endpoints', 'UserTrackSelection')
    UserRequest = apps.get_model('endpoints', 'UserRequest')
    SpotifyTrackSelection = apps.get_model('endpoints', 'SpotifyTrackSelection')
    Recommendation = apps.get_model('endpoints', 'Recommendation')

    songQStoDict = lambda y : {x[0]: {'title': x[1], 'main_artist': x[2]} for x in y}
    songQStoPKs = lambda y : [x[0] for x in y]
    deletedSongsDict = {}

    for row in SongQueryObject.objects.all():
        title = row.song_name
        main_artist = row.artist_name

        userSelectedSongQS = Song.objects.filter(
            title__iexact=title, main_artist__iexact=main_artist).values_list('id', 'title', 'main_artist')
        if userSelectedSongQS:
            userSelectedSong = userSelectedSongQS[0]   
            # delete duplicate songs based on Songs queried by user
            deletedSongsDict.update(songQStoDict(userSelectedSongQS[1:]))
            songsToDeleteIDs = songQStoPKs(userSelectedSongQS)
            Song.objects.filter(pk__in=songsToDeleteIDs[1:]).delete()

            # Populate user request 
            UserRequestObj = UserRequest(spotifySeeds='default')
            UserRequestObj.save()

            # Populate user selection
            userTrackSelectionObj = UserTrackSelection(requestObject=UserRequestObj, trackID=Song.objects.get(pk=userSelectedSong[0]))
            userTrackSelectionObj.save()

            # Populate recommendation
            RecommendationObj = Recommendation(
                userRequest=UserRequestObj
            )
            RecommendationObj.save()

            # Populate spotify selection
            spotifySelectionObjList = []
            recommendation_ids_list = row.recommendation_ids.split(', ')
            for old_id in recommendation_ids_list:
                if int(old_id) in deletedSongsDict:
                    deletedSongInfo = deletedSongsDict[int(old_id)]
                    recommendedSongObj = Song.objects.filter(
                        title=deletedSongInfo['title'], 
                        main_artist=deletedSongInfo['main_artist']
                    )
                    if len(recommendedSongObj) > 1:
                        allSongEntriesQS = Song.objects.filter(
                            title=deletedSongInfo['title'], 
                            main_artist=deletedSongInfo['main_artist']
                        ).values_list('id', 'title', 'main_artist')
                        songsToDeleteIDs = songQStoPKs(allSongEntriesQS)
                        idx = 0 if int(old_id) not in songsToDeleteIDs else list(songsToDeleteIDs).index(int(old_id))
                        allSongEntriesQS = list(allSongEntriesQS)
                        del allSongEntriesQS[idx]
                        del songsToDeleteIDs[idx]
                        deletedSongsDict.update(songQStoDict(allSongEntriesQS))
                        Song.objects.filter(pk__in=songsToDeleteIDs).delete()

                        recommendedSongObj = Song.objects.filter(
                            title=deletedSongInfo['title'], 
                            main_artist=deletedSongInfo['main_artist']
                        )[0]
                    else:
                        recommendedSongObj = recommendedSongObj[0]
                else:
                    recommendedSongObj = Song.objects.filter(pk=old_id).first()
                    allSongEntriesQS = Song.objects.filter(
                        spotify_id=recommendedSongObj.spotify_id).values_list('id', 'title', 'main_artist')

                    # delete duplicate songs based on Songs recommended by spotify
                    songsToDeleteIDs = songQStoPKs(allSongEntriesQS)
                    idx = list(songsToDeleteIDs).index(int(old_id))
                    allSongEntriesQS = list(allSongEntriesQS)
                    del allSongEntriesQS[idx]
                    del songsToDeleteIDs[idx]
                    deletedSongsDict.update(songQStoDict(allSongEntriesQS))
                    Song.objects.filter(pk__in=songsToDeleteIDs).delete()

                spotifySelectionObjList.append(SpotifyTrackSelection(
                    requestObject=RecommendationObj,
                    trackID=recommendedSongObj
                ))
            SpotifyTrackSelection.objects.bulk_create(spotifySelectionObjList)
    print(len(deletedSongsDict))


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0012_add_new_models'),
    ]

    operations = [
        migrations.RunPython(populateRecommendations)
    ]
