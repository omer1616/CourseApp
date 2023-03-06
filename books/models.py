import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250)
    tagline = models.TextField(verbose_name="Kısa Açıklama", blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, editable=False)
    image = models.ImageField(upload_to="book", verbose_name="Kapak Fotoğrafı", blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="aouthor_books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_books")
    description = models.TextField(max_length=500, blank=True, null=True)
    pricice = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    relase_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"
        # db_table = 'book_test'
        # ordering = ['created_date']

    # def save(self):
    #     letters = string.ascii_lowercase
    #     random_letters = ''.join(random.choice(letters) for i in range(10))
    #     self.slug = slugify(self.name + '-' + random_letters)
    #
    #     super(Book, self).save()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"books/{self.slug}"
        return reverse('book_detail', kwargs={'slug': self.slug})


EVALUATİON = (
    ('1', 'Kötü'),
    ('2', 'Eh İşte'),
    ('3', 'İdare Eder'),
    ('4', 'İyi'),
    ('5', 'Çok iyi'),

)
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Kitap", on_delete=models.CASCADE)
    comment = RichTextField()
    evulation = models.CharField(max_length=25, choices=EVALUATİON,  default=5)

    def __str__(self):
        return f" {self.book} - {self.user} - {self.comment}"
