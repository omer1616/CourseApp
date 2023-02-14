from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .form import BookForm
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


def get(request):
    if request.method == "GET":
        name = request.GET.get('name')
        print(name)
        tagline = request.GET.get('tagline')
        print(tagline)
        context = {
            'name': name,
            'tagline': tagline
        }

    return render(request, 'get.html', context=context)


def post(request):
    if request.method == "POST":
        name = request.POST.get('name')

        print(name)
        context = {
            'name': name
        }
        return render(request, 'post.html', context=context)

    return render(request, 'post.html')


def create_book(request):
    form = BookForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }

    return render(request, 'form.html', context=context)


def post_update(request):
    pass