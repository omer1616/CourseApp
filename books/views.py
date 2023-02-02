from django.shortcuts import render
from django.http import HttpResponse,  JsonResponse

# Create your views here.

def home(request):
    data = f"Merhaba burası home sayfası"
    context = {
        'data': data
    }
    return render(request, 'index.html', context=context)

def books(request):
    data = f"Merhaba burası boks sayfası" 
    return HttpResponse(data)







