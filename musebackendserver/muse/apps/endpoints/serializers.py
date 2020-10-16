from rest_framework import serializers

from .models import (Endpoint, AlgorithmStatus, 
                    MLAlgorithm, NLPObject, NLPRequest)


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ("id", "name", "owner", "created_at")
        fields = read_only_fields


class MLAlgorithmSerializer(serializers.ModelSerializer):

    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return AlgorithmStatus.objects.filter(
            parent_mlalgorithm=mlalgorithm).latest(
                'created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = ("id", "name", "description", "code",
                            "version", "owner", "created_at",
                            "parent_endpoint", "current_status")
        fields = read_only_fields


class AlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at",
                "parent_mlalgorithm")


class NLPRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NLPRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields =  (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "created_at",
            "parent_mlalgorithm",
        )