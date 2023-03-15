from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import books, book_detail, home
from books.models import *


# class TestUrls(SimpleTestCase):
#
#     def test_list_url_resolved(self):
#         url = reverse('books')
#         # print(resolve(url))
#
#         self.assertEqual(resolve(url).func, books)
#
#     def test_detail_url_resolves(self):
#
#         url = reverse('book_detail', kwargs={'slug': 'slug'})
#         self.assertEqual(resolve(url).func, book_detail)
