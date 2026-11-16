from django_filters import rest_framework as filters

from library.models import Book


class BookFilter(filters.FilterSet):
    # Case-insensitive partial match on the book title
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'year_published', 'genres']
