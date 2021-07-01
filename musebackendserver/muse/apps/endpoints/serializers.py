import json

from .models import Song, UserRequest, Recommendation, UserTrackSelection, SpotifyTrackSelection

from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class UserTrackSelectionSeriializer(serializers.ModelSerializer):

    class Meta:
        model = UserTrackSelection
        fields = '__all__'


class SpotifyTrackSelectionSeriializer(serializers.ModelSerializer):

    class Meta:
        model = SpotifyTrackSelection
        fields = '__all__'


class SongRequestSerializer(serializers.Serializer):
    song = serializers.CharField(max_length=50)
    artist = serializers.CharField(max_length=50)
    spotifyObj = serializers.JSONField()

    def validate_spotifyObj(self, value):
        '''
        Check valid JSON and  return formatting errors
        '''
        try:
            value = json.loads(value)
        except Exception as err:
            json_error_str = f'Invalid JSON! {err}'
            raise serializers.ValidationError(json_error_str)
        return value


class RecommendationIDRequestSerializer(serializers.Serializer):
    recommendation_id = serializers.UUIDField()