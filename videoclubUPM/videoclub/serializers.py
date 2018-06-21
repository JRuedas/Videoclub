from rest_framework import serializers
from videoclub.models import Movie, Cast

# http://www.django-rest-framework.org/api-guide/serializers/

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id_movie', 'title', 'overview', 'date', 'director', 'url_poster', 'vote_average', 'url_video', 'budget', 'revenue', 'original_language', 'status')


class CastSerializer(serializers.ModelSerializer):

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Cast
        fields = ('name', 'movies')