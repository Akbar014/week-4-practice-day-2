from django.shortcuts import render
from album.models import Album
from musician.models import Musician

def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data' : data})