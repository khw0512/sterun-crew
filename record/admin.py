from django.contrib import admin
from record.models import *

# Register your models here.
admin.site.register(Record)
admin.site.register(PersonalRecord)
admin.site.register(Team)
admin.site.register(TeamMember)