from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_forms = forms.AlbumForm(request.POST)
        if album_forms.is_valid():
            album_forms.save()
    album_forms = forms.AlbumForm
    return render (request, 'album.html',{'forms' : album_forms})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_forms = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_forms = forms.AlbumForm(request.POST, instance=album)
        if album_forms.is_valid():
            album_forms.save()
            return redirect('home')
    return render (request, 'album.html',{'forms' : album_forms})
        
def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')

    
    

