from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_summernote.fields import SummernoteTextField


def image_upload_path(instance, filename):
    return f'article/{instance}/{filename}'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    content = SummernoteTextField()
    main_img = models.ImageField(upload_to=image_upload_path)
    brand = models.CharField(max_length=30)
    bgmusic = models.CharField(max_length=50)
    model = models.CharField(max_length=30)
    desc = models.TextField()
    pay = models.BooleanField(default=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title