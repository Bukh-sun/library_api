from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book, Genre
from datetime import datetime

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(first_name='Varlam', last_name='Shalamov',
                                                   country='Soviet Union', birth_date=datetime(1933, 12, 17))
        self.book = Book.objects.create(
            title='Shock therapy',
            author=self.author,
            year_published=1969,
            description='Stories about labour camps'
        )
        self.book2 = Book.objects.create(
            title='Shock therapy2',
            author=self.author,
            year_published=1970,
            description='Stories about labour camps and terror'
        )

    def test_get_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data['results']
        self.assertGreaterEqual(len(books), 1)