from django.urls import path

from .views import AllCommentsView, SongCreateView
from .views import SongDeleteView, SongListView, SongUpdateView


urlpatterns = [
    path("song_list", SongListView.as_view(), name="song_list"),
    path("song_create/", SongCreateView.as_view(), name="song_create"),
    path("song_update/<int:pk>/", SongUpdateView.as_view(), name="song_update"),
    path("song_delete/<int:pk>/", SongDeleteView.as_view(), name="song_delete"),
    path('music/<int:music_id>/all_comments/', AllCommentsView.as_view(), name='all_comments'),
]
