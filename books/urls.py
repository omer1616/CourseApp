from django.urls import path

from . import views


urlpatterns = [
    path('', views.books),
    path('home/', views.home),
    path('books/',  views.books),
    path('books/<slug>', views.book_detail,  name="book_detail"),
    path('get', views.get,  name="get"),
    path('post', views.post,  name="post"),
]