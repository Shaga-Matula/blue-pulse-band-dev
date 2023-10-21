from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

def validate_mp3_file(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError('Only MP3 files are allowed.')

class MusicMod(models.Model):
    artist_name = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    song_file = CloudinaryField('raw', resource_type='auto', validators=[validate_mp3_file])
    song_image = CloudinaryField('image', default='placeholder')

    
    def __str__(self):
        return f"{self.artist_name} - {self.song_title}"
