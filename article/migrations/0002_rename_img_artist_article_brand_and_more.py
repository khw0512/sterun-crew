# Generated by Django 5.1.4 on 2025-04-06 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img_artist',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='music_artist',
            new_name='model',
        ),
    ]
