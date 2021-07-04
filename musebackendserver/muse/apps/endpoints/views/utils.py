from ..models import Song

def get_tracks_dict_from_recommendation_object(recommendations):
    # RelatedManager backward query using `related_name` attribute of FK
    recommended_tracks_IDs = list(
        map(
            lambda x: x.hex, 
            recommendations.selectedTracks.all().values_list('track', flat=True)
        )
    )
    recommended_tracks = list(Song.objects.filter(pk__in=recommended_tracks_IDs).values())

    return {
        'recommendation_id': recommendations.id.hex,
        'recommended_track_ids': recommended_tracks_IDs,
        'recommended_tracks': recommended_tracks
    }