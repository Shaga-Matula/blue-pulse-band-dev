from django.db import models


class MusicMod(models.Model):
    artist_name = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    song_file = models.FileField(upload_to='songs/')
    song_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.song_title
