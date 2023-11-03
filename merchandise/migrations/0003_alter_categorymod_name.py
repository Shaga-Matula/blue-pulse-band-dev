# Generated by Django 3.2.22 on 2023-11-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_alter_categorymod_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymod',
            name='name',
            field=models.CharField(choices=[('clothes', 'Clothes'), ('memorabilia', 'Memorabilia'), ('cd', 'CD')], max_length=254, verbose_name='Category Name'),
        ),
    ]
