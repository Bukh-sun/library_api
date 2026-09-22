from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from library.models import Book, Author, Genre
from library.serializers import BookSerializer, BookCreateUpdateSerializer, AuthorSerializer, GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('genres')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookCreateUpdateSerializer
        else:
            return BookSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author', 'year_published', 'genres']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books')
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.prefetch_related('books')
    serializer_class = GenreSerializer