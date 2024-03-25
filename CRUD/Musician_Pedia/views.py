from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Musician_Pedia.forms import MusicianForm, AlbumForm
from Musician_Pedia.models import Musician, Album
from django.db.models import Avg


# Create your views here.


def home(request):
    musicinan_list = Musician.objects.all().order_by('first_name')
    dictionary = {
        'title':'Home',
        'musician_list':musicinan_list
    }
    return render(request, 'index.html', context=dictionary)

def add_artist(request):
    form = MusicianForm()
    dictionary = {
        'title':'Add Artist',
        'form': form,
    }
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'artist_form.html', context=dictionary)

def add_album(request):
    form = AlbumForm()
    dictionary = {
        'title':'Add Album',
        'form': form,
    }
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'album_form.html', context=dictionary)


def album_list(request , artist_id ):
    list_of_album = Album.objects.filter(name_id=artist_id).order_by('release_date')
    artist = Musician.objects.get(pk = artist_id )
    rate = Album.objects.filter(name_id = artist_id).aggregate(Avg('album_ratings'))
    dictionary ={
        'title':'List Albums',
        'list_of_album':list_of_album,
        'artist':artist,
        'rate':rate
    }
    return render(request, 'album_list.html', context=dictionary)


def update_album(request, album_id, artist_id):
    artist = Musician.objects.get(pk=artist_id)
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album)
    dictionary = {
        'title': "Updating Album",
        'form': form,
    }
    if request.method == 'POST':
        form = AlbumForm( request.POST, instance= album )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Musician_Pedia:album_list', args=[artist_id]))
    return render(request, 'update_album.html', context=dictionary)


def update_artist(request, artist_id):
    artist = Musician.objects.get(pk=artist_id)
    form = MusicianForm(instance=artist)
    dictionary ={
        'title': "Updating Artist",
        'form': form,
    }
    if request.method == 'POST':
        form = MusicianForm( request.POST, instance= artist )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'update_artist.html', context=dictionary)

def delete_artist(request , artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()
    dictionary ={
        'title': "Delete Artist",
        'alert': "Sucessfully Deleted The Artist"
    }
    return render(request, 'delete.html', context=dictionary)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    dictionary = {
        "title": "Delete Album",
        "alert": "Sucessfully Deleted The Album"
    }
    return render(request, 'delete.html', context=dictionary)