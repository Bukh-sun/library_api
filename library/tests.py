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
        self.author2 = Author.objects.create(first_name='Boris', last_name='Kagar',
                                             country='Russia', birth_date=datetime(1945, 12, 23))
        self.genre = Genre.objects.create(name='Test genre', brief_description='Test genre description')
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
        self.book3 = Book.objects.create(
            title='Periphery empire',
            author=self.author2,
            year_published=1960,
            description='History and geopolitics'
        )

    def test_get_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data['results']
        self.assertGreaterEqual(len(books), 1)

    def test_get_author_books(self):
        response = self.client.get(f'/api/books/?author={self.author2.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data['results']
        self.assertGreaterEqual(len(books), 1)
        for book in books:
            self.assertEqual(book['author_detail']['id'], self.author2.id)

    def test_create_book(self):
        url = '/api/books/'
        data = {
            'title': 'Kolyma tells',
            'author': self.author.id,
            'year_published': 1955,
            'description': 'Stories about labour camps',
            'genres': [self.genre.id],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)