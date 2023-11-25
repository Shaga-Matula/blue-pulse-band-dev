from django.db import models


class NewsLetterMod(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"

    def __str__(self):
        return self.email



