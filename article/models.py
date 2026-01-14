from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django_summernote.fields import SummernoteTextField


def image_upload_path(instance, filename):
    return f'article/{instance.uuid}/{filename}'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    content = SummernoteTextField()
    main_img = models.ImageField(upload_to=image_upload_path)
    brand = models.CharField(max_length=30, blank=True, null=True)
    bgmusic = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=30)
    desc = models.TextField()
    pay = models.BooleanField(default=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title