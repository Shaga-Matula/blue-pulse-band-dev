from django.urls import path

from .views import SongCreateView, SongListView, SongUpdateView

urlpatterns = [
    path("song_list", SongListView.as_view(), name="song_list"),
    path("song_create/", SongCreateView.as_view(), name="song_create"),
    path("song/update/<int:pk>/", SongUpdateView.as_view(), name="song_update"),
]
