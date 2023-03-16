from django.urls import path

from . import views


urlpatterns = [
    path('', views.books),
    path('home/', views.home),
    path('books/',  views.books, name='books'),
    path('books/<slug>', views.book_detail,  name="book_detail"),
    path('get', views.get,  name="get"),
    path('post', views.post,  name="post"),
    path('create-book', views.create_book,  name="create_book"),
    path('books/<slug>/update', views.update_book, name="update_book"),
    path('books/<int:id>/remove', views.remove_book, name="remove_book"),
    path('create-comment', views.create_comment, name="comment"),
    path('search/', views.search, name="search"),
]