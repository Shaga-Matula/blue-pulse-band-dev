from cloudinary.models import CloudinaryField
from django.db import models

from profiles.models import UserProfile


class MusicMod(models.Model):
    artist_name = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    song_file = CloudinaryField("song_file", resource_type="auto")
    song_image = CloudinaryField("song_image", default="placeholder")

    def __str__(self):
        return f"{self.artist_name} - {self.song_title}"


class CommentMod(models.Model):
    music = models.ForeignKey(MusicMod, on_delete=models.CASCADE, related_name='comments')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    reply_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')

    def __str__(self):
        user = self.user_profile.user
        return f"Comment by {user.username} on {self.music.artist_name} - {self.music.song_title}"
