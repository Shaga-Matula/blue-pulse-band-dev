from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import (
    AddCommentToSongView,
    CommentDeleteView,
    ContactUsView,
    DisLikeCommentView,
    LikeCommentView,
    SongCommentEditView,
    SongCreateView,
    SongDeleteView,
    SongListCommentView,
    SongListView,
    SongUpdateView,
    handler404,
)

urlpatterns = [
    path("song_list", SongListView.as_view(), name="song_list"),
    path("song_create/", SongCreateView.as_view(), name="song_create"),
    path("song_update/<int:pk>/", SongUpdateView.as_view(), name="song_update"),
    path("song_delete/<int:pk>/", SongDeleteView.as_view(), name="song_delete"),
    # Comments
    path("song_all_comments/", SongListCommentView.as_view(), name="song_all_comments"),
    path(
        "song/<int:pk>/add_comment/",
        AddCommentToSongView.as_view(),
        name="add_comment_to_song",
    ),
    path("comment/edit/<int:pk>/", SongCommentEditView.as_view(), name="edit_comment"),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"
    ),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
    path("like/<int:pk>/", LikeCommentView.as_view(), name="like_post"),
    path("dislike/<int:pk>/", DisLikeCommentView.as_view(), name="dis_like_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "musicapp.views.handler404"
