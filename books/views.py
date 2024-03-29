from django.shortcuts import render, get_object_or_404, redirect ,reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .form import BookForm, CommentForm
# Create your views here.
from .models import Book, Author
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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
        print("***" * 10)
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

@csrf_exempt
def remove_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()

    return JsonResponse({'status': True})



def create_comment(request):

    form = CommentForm(request.POST or None)
    if form.is_valid():

          form.save()
          print("kaydedildi")

    return render(request, 'book/comment.html', context={'form': form})


def search(request):
    from django.db.models import Q
    if request.method == "GET":
        searched = request.GET['search']

        print("**"*25)
        books = Book.objects.filter(
            Q(name__icontains=searched) | Q(category__name__icontains=searched) | Q(pricice__icontains=searched))
        context = {'searched': searched,
                    'books': books}

        return render(request, "book/search.html", context=context)