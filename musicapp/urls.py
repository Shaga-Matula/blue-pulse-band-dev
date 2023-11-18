from django.urls import path

from .views import SongCreateView, SongListCommentView
from .views import SongDeleteView, SongListView, SongUpdateView


urlpatterns = [
    path("song_list", SongListView.as_view(), name="song_list"),
    path("song_create/", SongCreateView.as_view(), name="song_create"),
    path("song_update/<int:pk>/", SongUpdateView.as_view(), name="song_update"),
    path("song_delete/<int:pk>/", SongDeleteView.as_view(), name="song_delete"),
    path('song_all_comments/', SongListCommentView.as_view(), name='song_all_comments'),
]
