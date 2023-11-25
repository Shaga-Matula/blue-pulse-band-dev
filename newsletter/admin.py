from django.contrib import admin
from .models import NewsLetterMod

@admin.register(NewsLetterMod)
class NewsLetterModAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)