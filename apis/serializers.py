from rest_framework import serializers


class RestSerializer(serializers.Serializer):
    message = serializers.CharField()


class PopularMoviesSerializer(serializers.Serializer):
    top_n = serializers.IntegerField()


class GenreMovieSerializer(serializers.Serializer):
    genre = serializers.CharField()
    top_n = serializers.IntegerField()
