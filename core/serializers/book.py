from rest_framework import serializers

from .author import AuthorSerializer
from .genre import GenreSerializer
from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'genres', 'rating']
