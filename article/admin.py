from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.


@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',) 