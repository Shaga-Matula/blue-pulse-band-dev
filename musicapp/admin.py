from django.contrib import admin
from . models import MusicMod
from .models import CommentMod
# Register your models here.

class MusicModAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'song_title']
    search_fields = ['artist_name', 'song_title']

admin.site.register(MusicMod, MusicModAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user_profile', 'music', 'created_at', 'modified_at']
    list_filter = ['created_at', 'modified_at']
    search_fields = ['text', 'user_profile__user__username', 'music__artist_name', 'music__song_title']

admin.site.register(CommentMod, CommentAdmin)