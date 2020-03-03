from rest_framework import serializers


class RestSerializer(serializers.Serializer):
    message = serializers.CharField()
