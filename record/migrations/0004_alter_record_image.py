# Generated by Django 5.1.4 on 2025-03-31 13:17

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_remove_record_pace_remove_record_time_record_pace_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 500], upload_to='record'),
        ),
    ]
