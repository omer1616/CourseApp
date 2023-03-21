import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import itertools

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
    author = models.ManyToManyField(Author, related_name="author_books")
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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            for x in itertools.count(1):
                if not Book.objects.filter(slug=self.slug).exists():
                    break
                self.slug = slugify(self.name + '-' + str(x))
        super().save(*args, **kwargs)

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

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        # temporary solution, because the form currently only allows integer amounts
        total_expense_amount = int(total_expense_amount)

        return self.budget - total_expense_amount

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

    def get_absolute_url(self):
        return '/' + self.slug


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-amount',)
