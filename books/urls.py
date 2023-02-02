from django.urls import path

from . import views


urlpatterns = [
    path('', views.books),
    path('home/', views.home),
    path('books/',  views.books)

]