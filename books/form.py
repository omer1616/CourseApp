from django.forms import ModelForm,  TextInput
from .models import Book, Author, Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'category', 'pricice', 'image']
       


