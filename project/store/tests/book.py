from django.test import TestCase
from django.urls import reverse

from project.store.models import Book, User

from model_bakery import baker

import tempfile


class TestBookModel(TestCase):
    """basic test cases for book model"""

    def setUp(self):
        """create a book instance"""
        self.book = Book.objects.create(
            title='Book 1',
            price = 100,
            amount = 10,
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

    def test_create_bulk_books(self):
        """test creating 1000 books"""
        books = baker.make(Book, _quantity=1000)
        self.assertEqual(len(books), 1000)

    def test_books_list(self):
        """test book list view"""
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_book_exists(self):
        """check if the book is existed"""
        self.assertIsNotNone(self.book)

    def test_book_availability(self):
        """check that book amount is more than 0"""
        self.assertNotEqual(self.book.amount, 0)

    def test_get_book_absolute_url(self):
        """test book detail status code"""
        response = self.client.get(reverse('book-detail', args=[self.book.pk,]))
        self.assertEqual(response.status_code, 200)
