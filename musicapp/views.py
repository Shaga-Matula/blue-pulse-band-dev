from django.shortcuts import render
from .models import MusicMod

def song_list(request):
    songs = MusicMod.objects.all()
    return render(request, 'musicapp/song_list.html', {'songs': songs})

def ramble(request):
    songs = MusicMod.objects.all()
    return render(request, 'musicapp/ramble.html', {'songs': songs})