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
`values()` bu metod nesnelerimizi sözlüğe dönüştürmemizi sağlar 

```pycon
category =  Category.objects.filter(name="Roman").values()
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
















   
        
        
        







 
