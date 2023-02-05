from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .models import Book, Author


def home(request):
    data = f"Merhaba burası home sayfası"

    context = {
        'data': data
    }
    return render(request, 'index.html', context=context)


def books(request):
    books = Book.objects.all()
    x = False
    context = {'books': books,
               'x': x
               }
    return render(request, 'books.html', context=context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)
