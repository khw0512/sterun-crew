from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *



admin.site.register(MarathonEvent)
admin.site.register(MarathonReg)