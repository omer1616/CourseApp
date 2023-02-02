# Django Temellleri
## Sanal Ortam Kurulumu
`python3 -m venv env` <br/><br/>
**Sanal ortamı kurduktan sonra Aktif edelim**<br/>

*Linux ve Mac kullanıcıları için* <br/>  `source ./env/bin/activate`<br/><br/>
*Windows kullanıcıları için* <br/>  `myenv\Scripts\activate`

## Django Kurulumu<br/>
**Djangoyu sanal ortamımıza kuralım**<br/>
`pip install Django`<br/><br/>
**Daha sonra ilk Django uygulamımamızı oluşturalım**<br/>
`django-admin startproject core .`<br/><br/>

**Uygulamayı ayağa kaldıralım**<br/>
`python manage.py runserver`<br/><br/>


**App oluşturma**<br/>
`python manage.py startapp books`<br/><br/>

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

   
        
        
        







 
