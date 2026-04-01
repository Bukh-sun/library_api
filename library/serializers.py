from rest_framework import serializers

from library.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'country']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'brief_description']

class BookSerializer(serializers.ModelSerializer):
    author_detail = AuthorSerializer(source='author', read_only=True)
    genre_detail = GenreSerializer(source='genres',read_only=True, many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'year_published', 'author', 'genres', 'description', 'author_detail', 'genre_detail']

class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'year_published', 'author', 'genres']