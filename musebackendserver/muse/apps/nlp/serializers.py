from rest_framework import serializers

from apps.endpoints.serializers import RecommendationIDRequestSerializer


class ModelRequestSerializer(serializers.Serializer):
    recommendation_id = serializers.UUIDField()
    model_code = serializers.CharField(max_length=10)
