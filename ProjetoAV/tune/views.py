from django.shortcuts import render
from tune.models import Album
from tune.models import Musica
from tune.models import Artist

# Create your views here.

def index(request):

    return render(request, 'index.html')

def contact(request):
    listAr = Artist.objects.all()
    context = {
        'artistas': listAr
    }
    return render(request, 'contact.html',context)

def store(request):
    listM = Musica.objects.all()
    context = {
        'musicas': listM
    }
    return render(request, 'store.html', context)

def order(request):
    listA = Album.objects.all()
    context = {
        'albuns': listA
    }
    return render(request, 'order.html', context)