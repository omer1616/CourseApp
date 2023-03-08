# Django Temellleri
## Sanal Ortam Kurulumu
`python3 -m venv env` <br/><br/>
**Sanal ortamı kurduktan sonra Aktif edelim**<br/>

*Linux ve Mac kullanıcıları için* <br/>  `source ./env/bin/activate`<br/><br/>
*Windows kullanıcıları için* <br/>  `env\Scripts\activate`

## Django Kurulumu<br/>
**Djangoyu sanal ortamımıza kuralım**<br/>
`pip install Django`<br/><br/>
**Daha sonra ilk Django uygulamımamızı oluşturalım**<br/>
`django-admin startproject core .`<br/><br/>

**Uygulamayı ayağa kaldıralım**<br/>
`python manage.py runserver`<br/><br/>


**App oluşturma**<br/>
`python manage.py startapp books`<br/><br/>
**Uygulamamızı ana klasörümüzde olan `settings.py` dosyamıza şu şekilde tanıtalım**<br/>
`core/settings.py`<br/>
```py
INSTALLED_APPS = [
    'django.contrib.admin', # Yönetici sitesi .
    'django.contrib.auth', # Authentication kimlik doğrulama izinleri yönetir
    'django.contrib.contenttypes', #İçerik türleri 
    'django.contrib.sessions', # Oturum sistemi session çerezleri tutmamıza olanak tanır
    'django.contrib.messages', # Mesajşalma çerçevesi 
    'django.contrib.staticfiles', # Static dosya işlemlerimiz için

    
    'books',
 
]
```
**İlk View'ı Oluşturma**
<br/>
`books/view.py`
<br/>

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the books index.")<br/>
``` 


`books/urls.py`<br/>

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
``` 
<br/>


`core/urls.py`<br/>

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
]
``` 

## Veritananı Kurulumu<br/>

**Öncelikle bize default olarak gelen veritabanı tablolarını  oluşturma için shell'de bu kodu kullanalım**<br/>
`python manage.py migrate`

## Model oluşturma<br/> 
**Modellerimizi oluşturuyoruz**
`books/models.py`

```py
class Category(models.Model):
    name = models.CharField(max_length=250)

  
class Author(models.Model):
    name = models.CharField(max_length=250)
    number_book = models.IntegerField(blank=True, null=True)

  
class Book(models.Model):
    name = models.CharField(max_length=250) # Veritabanındaki karakter verisi için kullanılan bir alandır. Örneğin, bir kişinin adını saklamak için 
    author = models.ManyToManyField(Author, related_name="author") # Veritabanındaki ManyToManyField(çoka çok) ilişkileri tutar .
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Veritabanındaki ForeignKey(bire çok) ilişkileri tutar
    description = models.TextField(max_length=500, blank=True, null=True) #Veritabanındaki integer veri tiplerini tutar 
    pricice = models.FloatField() # veritabanında float türleri tutar #Veritabanındaki float veri tiplerini tutar Örneğin, bir ürünün fiyatı.
    created_date = models.DateTimeField(auto_now_add=True)  #Veritabanındaki tarih verisi için kullanılan bir alandır
    relase_date = models.DateField(blank=True, null=True) #Veritabanındaki tarih verisi için kullanılan bir alandır
    is_active = models.BooleanField(default=True) # Veritabanındaki maktıksal verileri tutmak için kullanılır True/False değerleri alır
```



*Migrate alma**<br/>
`python manage.py makemigrations`<br/>
`python manage.py migrate`<br/>


## Django ORM <br/>
*Veri tabanı yönetimi için kullanılan tasarım kalıbıdır,  ORM verileri bir disin yapısına dönüştürerek daha kolay işlemler yapmamızı sağlar,  bu yaklaşımla  dilin kendi yapısına uygun veritabanı sorgulamaları yaparız*<br/>

**ORM İşlemleri**<br/>
*Terminal'e gidip python shell'imizi açıyoruz*<br/>

`python manage.py shell`<br/>

*Ardından Book sınıfımızı import ediyoruz*<br/>
```py 
from books.models import Book, Author, Category
```
**Veritabanı nesnesini oluşturma**<br/>
```pycon
author = Author(name="Yaşar Kemal")
author.save()
```
*Or*
```pycon
author = Author.objects.create(name="Yaşar Kemal", tagline="Yaşar Kemal....")
```
*create ile oluşturduktan sonra save etmemize gerek yoktur.*<br/><br/>
**Nesnelerdeki değişiklikleri kaydetme**
```pycon
author.name = "Orhan Kemal"
author.save()
```
***Nesneleri Çağrımak Filtrelemek***<br/>

*Veri Tabanındaki Bütün Nesneleri Getirmek*<br/>

```pycon
books =  Book.objects.all() #queryset döner
```
*Filtreme yapmak*<br/>

```pycon
books =  Book.objects.filter(name="Demirciler Çarşısı cinayeti") #queryset döner
```

*Sadece belirli bir nesneye ihticımız varsa kullanır(Dikkatli olmakta yarar var!)*<br/>

```pycon
books =  Book.objects.get(id=1) #queryset döner
```



***ForeignKey ve ManyToManyField alanlarını kaydetme***<br/>
**ForeignKey** *alanını kaydetmek*<br/> 


```pycon
from blog.models import Book, Category
book = Book.objects.get(pk=1)
category_roman = Category.objects.get(name="Roman")
book.category = roman_category
book.save()
```
**ManyToManyField** *alanını kaydetmek*<br/> 
*Bir ManyToManyField'ı güncellemek biraz farklı çalışır - ilişkiye bir kayıt eklemek için sahada add() yöntemini kullanın. Bu örnek, giriş nesnesine Author örneğini camus ekler:*
```pycon
from blog.models import Book, Author
camus = Author.objects.create(name="Albert Camus")
book.author.add(camus)
```

*Bir seferde birden çok kayıt ekleme*

```pycon
camus = Author.objects.create(name="Albert Camus")
dosto = Author.objects.create(name="dostoyevski")
seyma = Author.objects.create(name="Şeyma Subaşı")
book.author.add(camus, dosto, seyma)
```

## ORM Genel Sorgulamalar

*Bir üstte bahsettiğimiz `get()`, `filter()` gibi metodlar bazı durumlar için tek başına yeterli olamayabir bu nedenle ihtiyacımızın olabileceği giğer sorgu çeşiltlerine bakacağız*

`get_or_create()` bazı durumlarda oluşturmak istediğimiz nesneler eğer veri tabanında varsa istenmedik hatalarla karşılaşabiliriz bunu önlemek için kullanılan metod


```pycon

author, created = Author.objects.get_or_create(name="ömer", tagline="deneme")
```
*burada eğer varsa getirir yoksa oluşturur*<br/>
**Başka bir yöntem iste `get_or_404()`**
```pycon
from django.shortcuts import get_object_or_404
book = get_object_or_404(Book, id=1)
```
`exclude()` bu metod istenmeye ifadeyi hariç tutup diğerlerini döndürmek için kullanılır

```pycon
book = Book.objects.exclute(is_active=False)
```

`order_by()` bu metod nesnelerimizi sıralayarak çekmemize yarar 

```pycon
book = Book.objects.filter(is_active=True).order_by('created_date')
```
`reverse()` Sorgu kümesi öğelerinin döndürülme sırasını tersine çevirmek için yöntemi kullanılır 

```pycon
books = Book.objects.filter(is_active=True)
books.reverse()[:4]
```


`values()` bu metod nesnelerimizi sözlüğe dönüştürmemizi sağlar 

```pycon
category =  Category.objects.filter(name="Roman").values()
book = Book.objects.all()[1:3].values('id','name')
category
<QuerySet [{'id': 1, 'name': 'Roman'}]>

```
`values_list()` bu metod nesnelerimizi sözlük yerine Tuple olarak dönüştürmemizi sağlar 

```pycon
category =  Category.objects.values_list('id')
category
<QuerySet [(1,), (2,)]>
category =  Category.objects.values_list('id',flat=True)
category
<QuerySet [1, 2]>
```
`first()` bu metod ilk nesneyi döndürür 

```pycon
category = Category.objects.first()
```
`last()` bu metod son nesneyi döndürür 

```pycon
category = Category.objects.last()
```
`exists()` bu metod kontrol eder True veya False döndürür 

```pycon
category = Category.objects.filter(name="Roman").exists()
category
True
```

`count()` bu metod adet döndürür 

```pycon
a = Author.objects.count()
a
3
```
## Field Lookups

**Sorgulamalar fonksiyon içinde `__` iki alt çizgi şeklinde yapılır**<br/><br/>
*`exact` veri tabanında birebir aynı olanları getirir büyük küçük duyarlılığı vardır*

```pycon
Books.objects.filter(price__exact=100)
```
*`iexact` veri tabanında birebir aynı olanları getirir büyük küçük duyarlılığı yoktur*

```pycon
Books.objects.filter(name__iexact="İnce Memed")
```
*`contains` veri tabanında yerine bakılmaksızın içereni getirir*

```pycon
Blog.objects.filter(name__contains="Yaşar")
```
*`icontains` veri tabanında yerine bakılmaksızın içereni getirir büyük küçük duyarlılığı yoktur*

```pycon
Blog.objects.filter(name__icontains="Yaşar")
```
*`in` veri tabanında bir dizi içerisinde içerenleri getirir*

```pycon
a = Author.objects.filter(id__in=[1,2,3,4])
a
<QuerySet [<Author: Yaşar Kemal>, <Author: Orhan Kemal>, <Author: Şeyma Subaşı>]>
```
*`gt`  veri tabanında büyük olanları getirmek için*

```pycon
Blog.objects.update_or_create(price__gte=10)
```
*`gte`  veri tabanında büyük eşit olanları getirmek için*

```pycon
Blog.objects.filter(price__gte=10)
```
*`lt`  veri tabanında küçük olanları getirmek için*

```pycon
Blog.objects.update_or_create(price__lt=10)
```
*`gt`  veri tabanında küçük eşit olanları getirmek için*

```pycon
Blog.objects.update_or_create(price_lte=10)
```
*`startswith`  veri tabanında ile başlayanları*

```pycon
Blog.objects.filter(description_startswith="bu roman")
```
*`endswith`  veri tabanında ile bitenleri*

```pycon
Blog.objects.filter(description_endswith="bu roman")
```

## Q Nesnesi
*`Filter()` methodu içerisine yazdığımız argumanlar `And` ile birleşir `Or` kullanabilmemiz için `Q` nesnesinden yararlanırız.*



```pycon
from django.db.models import Q

books = Books.objects.filter(Q(stock_count=4), | Q(is_active=True))
products = Books.objects.filter(
    Q(price__gte=50) & Q(stock_count__gt=0)
)
```

## Django Admin 

**Meta Seçenekleri**


```py
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
        verbose_name = "Kitap" # tekil isimlendirme 
        verbose_name_plural = "Kitaplar" # Çoğul isimlendirme
        db_table = 'book_test'# veritabanında adı 
        ordering = ['created_date'] # sıralama
```

**Admin Özelleştirme Seçenekleri**

```py
from django.contrib import admin
from .models import Author, Category, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_date', 'is_active')  # listelenmek istenen fieldları göstermek icin
    list_filter = ('is_active', 'created_date', 'category')  # filtrelemek istediğimiz alanlar için kullanılır
    ordering = ('created_date',)  # sıralama icin kullanıkır
    search_fields = ('name', 'category', 'created_date', 'is_active')  # arama özelliğiæß
    list_per_page = 50  # sayfada kaç tane görünmesini istiyorsak
    actions = ('update_activate',)  # eklemek istediğimiz fonksiyon aksiyonlarını koyarız


    def update_activate(self, request, queryset):
        queryset.update(is_active=False)

    update_activate.short_description = "Seçili Nesneleri Yayına Al"  # actionun ismini düzenleme


admin.site.register(Author)
admin.site.register(Category)

```

## Django Template 

**Template yolunu verme**

**templates**

`core/settings.py` *dizininde template klasörümüzün yolunu tanıtıyoruz* 

````pycon
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
````
**Daha sonra ana dizine gelip `templates` adında klasör oluştuyoruz**
*oluşturduktan sonra `templates/index.html`* adında HTML dosyamızı oluşturalım

**View**

`books/view.py` dosyasına gidip ilgili fonksiyonumuza template html dosyamızın yolunu veriyoruz
````pycon
def home(request):
    data = f"Merhaba burası home sayfası"

    context = {
        'data': data
    }
    return render(request, 'index.html', context=context)
````   


## Template Veri gönderme
**View fonksiyonumuzu oluşturma ve verileri çekme**<br/>
`books/view.py` dosyasında books diye bir fonksiyon oluşturduktan sonra `Book.objects.all()`
metodumuzla tüm kitapları çekiyoruz yukarıda `context` adında bir dictionary içerinde datamızı gönderiyoruz. 

```python
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def books(request):
    books = Book.objects.all()
    x = False
    context = {'books': books,
               'x': x
               }
    return render(request, 'books.html', context=context)
```

**Url Dosyasına path'imzi tanıtma**<br/>
`books/urls.py` dosyamız;
```python
from django.urls import path

from . import views


urlpatterns = [
    path('', views.books),
    path('home/', views.home),
    path('books/',  views.books)

]
```
gibi olacak. <br/>


## HTML
**`HTML` içerisine verileri yazma**<br/>

*burada veriler bize bir queryset objesi olarak geleceğinde öncelikle bir for döngüsü içerisine alıp verilere ulaşabiliriz*


**For Kullanımı**<br/>

*`HTML` içerisine yazacağımız for döngüsü python kod bloğudur ama kullanımı biraz farklıdır.*

```html
{% for book in books %}
        <tr>
            <td>{{ book.name }}</td>
            <td>{{ book.category.name }}</td>
        </tr>
{% endfor %}
```


**ManyToMany için For Kullanımı**<br/><br/>
*burada bize bir `ManyToMany` ilişkisi döneceğinde yani bir kitabın birden fazla yazarı olabilir bu da demek oluyor ki birden fazla queryset objesi dönecek bunları almak için ayrıca tekrardan bir `for içerisinde` bütün yazarları çekmemiz gerekecek*

```html
 {% for book in books %}
        <tr>
            <td>{{ book.name }}</td>
            <td>{{ book.category.name }}</td>
            {% for authour in book.author.all %}
            <td> {{ authour.first_name }} </td>
                {%endfor%}
        </tr>
{% endfor %}
```
        
        
**If Kullanımı**<br/>

```html
  {% for book in books %}
        <tr>
            {% if book.name  != "Demirciler Çarşısı Cinayeti" %}
            <td>{{ book.name }}</td>
            <td>{{ book.category.name }}</td>
            {% for authour in book.author.all %}
            <td> {{ authour.first_name }} </td>
                {%endfor%}
          {% endif %}
            
        </tr>
{% endfor %}
```


## Book detay sayfası

*Detay sayfası o url'e gidildiğinde hangi ürün ise o ürüne ait özelliklerin sayfalandığı sayfalar*<br/>

**View**<br/>
*Burada fark edildiği üzere book_detail fonksiyonu request parametresinin yanına ayrı bir id parametresi aldı bunun nedeni biz objemizi çektiğimizde istek attığımız url'den gelen id nese gidip o id'li ürünü çekip önümüze çıkarması için*
````python
def book_detail(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)
````


**Url**

*detail sayfasını oluşturmak için ilgili url'e bir `/`' sonra bir `id` geleceğini bildirmek için bir parametre daha ekiyor ve ilgili fonksiyonumuzu çağırıyoruz*
 
````python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('home/', views.home),
    path('books/',  views.books),
    path('books/<int:id>', views.book_detail,  name="book_detail"), # name paramatresi html sayfalarında ilgili url'in pathini vermek için işimize yarayan kullanışlı bir parametre
]
````

**HTML**<br/>

*html sayfamızı templates klasörünün içerisinde oluşturalım `book_detail.html`* ardından sayfayı açtıktan sonra `book_detail` fonksiyonumuzdan gelen datayı çekebiliriz
````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{ book.name }}
</body>
</html>
````
*yukarıda fark ettiyseniz bir for dönmemize gerek kalmadı çünkü bir `queryset değil` `get` kullanarak tek bir obje çektik*<br/>


*son olarak `books.html` sayfasında ilgili url'i döndürecek 'href`'i verelim*

````html
     <td><a href="{% url 'book_detail'  book.id %}"> {{ book.name }}</a></td>
````

## Slug Oluşturma

*Slug, URL'leri daha anlamlı ve okunabilir hale getirmek için kullanılan bir veri tipidir.*<br/>
`books/models.py` sayfasına gidip save fonksiyonumuzu yazalım

```python
import random
import string
from django.db import models
from django.template.defaultfilters import slugify


     def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            for x in itertools.count(1):
                if not Book.objects.filter(slug=self.slug).exists():
                    break
                self.slug = slugify(self.name + '-' + str(x))
        super().save(*args, **kwargs)
```
**`get_absolute_url()`** kullanımı

``books/models.py`` dosyasına gidip alttaki fonksiyonu yazabiliriz <br/>

````python
def get_absolute_url(self):
   # return f"books/{self.slug}"
   return reverse('book_detail',  kwargs={'slug': self.slug})
````
ardından `templates/books.html` sayfasında ilgili fonksiyonumuzu çağırıyoruz

````html
        <tr>
{#            {% if book.name  != "Demirciler Çarşısı Cinayeti" %}#}
{#             {% url 'book_detail'  book.slug %}#}
            <td><a href="{{ book.get_absolute_url }}"> {{ book.slug }}</a></td>
            <td>{{ book.category.name }}</td>
            {% for authour in book.author.all %}
            <td> {{ authour.first_name }} </td>

                {%endfor%}
{#          {% endif %}#}
        </tr>

````

*bu şekilde url'lerimizi daha dinamiz kullanabiliriz.*


## Django Formlar


**GET isteği**

`view.py`

````python
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
````

`urls.py`

````python
path('get', views.get,  name="get"),
````


`get.html`

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form style="justify-content: right", method="GET">
    <label >isim</label>
    <input name="name">
     <label >açıklama</label>
    <input name="tagline">
    <button type="submit">kaydet</button>

    <h1>{{ name }}</h1>
    <h1>{{ tagline }}</h1>
</form>
</body>
</html>

````

**POST isteği**

`view.py`

````python
def post(request):
    if request.method == "POST":
        name = request.POST.get('name')

        print(name)
        context = {
            'name': name
        }
        return render(request, 'book/post.html', context=context)

    return render(request, 'book/post.html')
````

`urls.py`

````python
path('get', views.get,  name="get"),
path('post', views.post,  name="post"),
````


`post.html`

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="POST">
    {% csrf_token %}
    <label>Name</label>
    <input name="name">
    <label>Active</label>
    <input type="radio" id="vehicle3" name="active">

    <button type="submit">gönder</button>

</form>
</body>
</html>
````
**FORM ile oluşturma**

`form.py`

````python
from django.forms import ModelForm
from .models import Book, Author, Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'category', 'pricice']

````
`views.py`
````python
def create_book(request):
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'başarıyla oluşturuldu')
            return redirect('books')
    context = {
        'form': form
    }

    return render(request, 'book/form.html', context=context)

````

`urls.py`

````python
path('create-book', views.create_book,  name="create_book"),
````


`post.html`

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="POST">
     {% csrf_token %}

    {{ form.as_p }}
    <button type="submit">Ekle</button>
</form>
</body>
</html>
````
**FORM ile güncelleme**

`form.py`

````python
from django.forms import ModelForm
from .models import Book, Author, Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'category', 'pricice']

````
`views.py`
````python
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

````

`urls.py`

````python
path('create-book', views.create_book,  name="create_book"),
path('books/<slug>/update', views.update_book, name="update_book"),
````


`post.html`

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="POST">
     {% csrf_token %}

    {{ form.as_p }}
    <button type="submit">Ekle</button>
</form>
</body>
</html>
````


**Silme**


`views.py`
````python
def remove_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.delete()

    return redirect('books')

````

`urls.py`

````python
path('create-book', views.create_book,  name="create_book"),
path('books/<slug>/update', views.update_book, name="update_book"),
path('books/<slug>/remove', views.remove_book, name="remove_book"),
````

## Static Dosyalar

`static/index.css` dosyası oluşturuyorum

````css
body {
    background-color: red;
}

th {
    background: aqua;
}
````

`core/settings.py` dosyasında static ayarlarımı yapıyorum


````python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```` 
**Ayarları yaptıntan sonra  ``HTML` sayfamızda ilgili static dosyaları cagırıyoruz**

````html
{%  load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{% static 'css/index.css' %}">
</head>
<body>
<form style="justify-content: right", method="GET">
    <label >isim</label>
    <input name="name">
     <label >açıklama</label>
    <input name="tagline">
    <button type="submit">kaydet</button>

    <h1>{{ name }}</h1>
    <h1>{{ tagline }}</h1>
</form>
</body>
</html>
````



## HTML Dosyaları 

*base mantığı inculude, extend, content*<br/>

## Crispy Form

```pycon
pip install django-crispy-forms
pip install crispy-bootstrap5 
```


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user',
    'books',
    'get_post',
    'crispy_forms',
    'crispy_bootstrap5',
]
```
````html
{% extends "base.html" %}
{% load static %}
{% block content %}
{% load crispy_forms_tags %}

<form action="#" method="POST" enctype="multipart/form-data">
 {% csrf_token %}
  <div class="form-group">

  {{ form|crispy }}
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>

{% endblock %}
````

## Upload Image
```pycon
pip install Pillow
```
`books/models.py`
```python
class Book(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, editable=False)
    image = models.ImageField(upload_to="book", verbose_name="Kapak Fotoğrafı", blank=True, null=True)
```

`core/settings.py`

```python

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

`core/ulrs.py`

```python

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

`view.py`
```python
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

```
``form.html``
```html

<form action="#" method="POST" enctype="multipart/form-data">
 {% csrf_token %}
  <div class="form-group">

  {{ form|crispy }}
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>

{% endblock %}
```
## Ckeditor
`models.py`
````python
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Kitap", on_delete=models.CASCADE)
    comment = RichTextField()

    def __str__(self):
        return f" {self.book} - {self.user} - {self.comment}"
````

`forms.py`
```python
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

```
`views.py`
```python
def create_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'book/comment.html', context={'form': form})

```

`urls.py`
```python
path('create-comment', views.create_comment, name="comment"),

```
`comment.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">gönder</button>

</form>

<script type="text/javascript" src="{% static "ckeditor/ckeditor-init.js" %}"></script>
<script type="text/javascript" src="{% static "ckeditor/ckeditor/ckeditor.js" %}"></script>
</body>
</html>

```



`pip install django-ckeditor`

`core/settings.py`
````python

INSTALLED_APPS = [
   ...
    'ckeditor',

]
STATIC_ROOT = 'staticfiles/'
````
````pycon
python manage.py collectstatic
````












