from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250)
    tagline = models.TextField(verbose_name="Kısa Açıklama", blank=True, null=True)


    def __str__(self):
        return self.first_name + self.last_name


class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, related_name="author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, null=True)
    pricice = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    relase_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "kitap"
        verbose_name_plural = "kitaplar"
        # db_table = 'book_test'
        # ordering
