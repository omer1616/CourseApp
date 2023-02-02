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
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    years = models.IntegerField(blank=True, null=True)

  
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












   
        
        
        







 
