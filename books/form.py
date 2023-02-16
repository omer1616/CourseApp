from django.forms import ModelForm, TextInput
from .models import Book, Author, Category, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'category', 'pricice', 'image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
