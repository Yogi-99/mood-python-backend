from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apis import serializers
from services import chatbot, tone_analyzer, top_movies_based_on_genres
from models.Tone import Tone


class RestAPIView(APIView):
    serializer_class = serializers.RestSerializer

    def get(self, request, format=None):
        result = [1, 2, 3, 4, 5, 6]
        return Response({'message': 'hello', 'result': result})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('message')
            reply = chatbot.chat(name)
            tones = tone_analyzer.detect_tone(name)
            print(f'tones: {tones}')
            return Response({'reply': reply, 'tone_id': map(lambda t: t.tone_id + ' ' + str(t.score), tones)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopularMoviesRestAPIView(APIView):
    serializer_class = serializers.PopularMoviesSerializer

    def get(self, request, format=None):
        result = [1, 2, 3, 4, 5, 6]
        return Response({'message': 'hello', 'result': result})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            top_n = serializer.validated_data.get('top_n')
            result = top_movies_based_on_genres.get_top_n_popular_movies(top_n)
            return Response({'status': 'success', 'result': result})
        else:
            return Response({"status": 'fail'})


class GenreMoviesRestAPIView(APIView):
    serializer_class = serializers.GenreMovieSerializer

    def get(self, request, format=None):
        result = [1, 2, 3, 4, 5, 6]
        return Response({'message': 'hello', 'result': result})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            genre = serializer.validated_data.get('genre')
            top_n = serializer.validated_data.get('top_n')
            result = top_movies_based_on_genres.get_top_movies_filtered_by_genres(genre, top_n)
            return Response({'status': 'success', 'genre': genre, 'result': result})
        else:
            return Response({"status": 'fail'})
