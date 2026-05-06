from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from library.models import Book
from library.serializers import BookSerializer, BookCreateUpdateSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    ordering = ('id',)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookCreateUpdateSerializer
        else:
            return BookSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author', 'year_published', 'genres']