# Generated by Django 3.2.22 on 2023-11-21 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0006_rename_contact_contactmod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmod',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='commentmod',
            name='dislikes',
            field=models.ManyToManyField(related_name='comment_dis_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='commentmod',
            name='likes',
        ),
        migrations.AddField(
            model_name='commentmod',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
