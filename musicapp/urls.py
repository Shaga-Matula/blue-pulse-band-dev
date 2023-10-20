from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("song_list", views.song_list, name="song_list"),
]