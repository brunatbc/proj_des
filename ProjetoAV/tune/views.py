from django.shortcuts import render
from tune.models import Album

# Create your views here.

def index(request):
    listA = Album.objects.all()
    context = {
        'albuns': listA
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def store(request):
    return render(request, 'store.html')

def order(request):
    return render(request, 'order.html')