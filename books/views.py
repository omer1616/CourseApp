from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .form import BookForm
# Create your views here.
from .models import Book, Author
from django.contrib import messages


def home(request):
    data = f"Merhaba burası home sayfası"

    context = {
        'data': data
    }
    return render(request, 'base.html', context=context)


def books(request):
    books = Book.objects.all()
    x = False
    context = {'books': books,
               'x': x
               }
    return render(request, 'book/books.html', context=context)


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context=context)


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

    return render(request, 'book/get.html', context=context)


def post(request):
    if request.method == "POST":
        name = request.POST.get('name')

        print(name)
        context = {
            'name': name
        }
        return render(request, 'book/post.html', context=context)

    return render(request, 'book/post.html')


def create_book(request):
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
        print("***"*10)
        form.save()
        messages.success(request, 'başarıyla oluşturuldu')
        return redirect('create_book')

    context = {
        'form': form
    }

    return render(request, 'book/form.html', context=context)


def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    print(book)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        book.save()
    print(form)
    context = {
        'form': form
    }

    return render(request, 'book/book_update.html', context=context)


def remove_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.delete()

    return redirect('books')
