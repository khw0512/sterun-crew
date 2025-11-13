from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField

class MarathonEvent(models.Model):
    marathon_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    date_time = models.DateTimeField()
    location_city = models.CharField(max_length=50)
    location_cource = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return str(self.title)
    

class MarathonReg(models.Model):
    marathon = models.ForeignKey(MarathonEvent, on_delete=models.CASCADE)
    distance = models.CharField(max_length=10, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.marathon) +"_"+ str(self.user)