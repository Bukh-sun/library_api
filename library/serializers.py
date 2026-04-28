from django.core.validators import MaxValueValidator
from django.utils import timezone
from rest_framework import serializers

from library.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'country', 'birth_date']
        read_only_fields = ['id']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'brief_description']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    author_detail = AuthorSerializer(source='author', read_only=True)
    genre_detail = GenreSerializer(source='genres',read_only=True, many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'year_published', 'genre_detail', 'description', 'author_detail']

class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'year_published', 'author', 'genres']