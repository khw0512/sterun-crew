# Generated by Django 5.1.4 on 2025-03-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
