# Generated by Django 3.2.22 on 2023-11-20 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20231120_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_last_name',
        ),
    ]
