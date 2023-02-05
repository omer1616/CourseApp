import random
import string
from django.db import models
from django.template.defaultfilters import slugify


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
    author = models.ManyToManyField(Author, related_name="author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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

    def save(self):
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for i in range(10))
        self.slug = slugify(self.name + '' + random_letters)
        super(Book, self).save(self)
