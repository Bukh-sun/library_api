from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from library.models import Book, Author, Genre
from library.permissions import IsOwnerOrReadOnly
from library.serializers import BookSerializer, BookCreateUpdateSerializer, AuthorSerializer, GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    queryset = Book.objects.select_related('author').prefetch_related('genres')
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author', 'year_published', 'genres']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookCreateUpdateSerializer
        else:
            return BookSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books')
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.prefetch_related('books')
    serializer_class = GenreSerializer