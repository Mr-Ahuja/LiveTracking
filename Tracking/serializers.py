from rest_framework import serializers

from .models import Logs

class LogsSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    time = serializers.DateTimeField()

    def create(self, validated_data):
        return Logs.objects.create(**validated_data)