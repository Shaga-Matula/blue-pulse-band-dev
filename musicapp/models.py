from django.db import models


class MusicMod(models.Model):
    artist_name = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    song_file = models.FileField(null=True, blank=True)
    song_image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.song_title
