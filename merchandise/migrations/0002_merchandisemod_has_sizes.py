# Generated by Django 3.2.22 on 2023-11-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandisemod',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
