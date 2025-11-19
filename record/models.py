from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField

# def image_upload_path(instance, filename):
#    time = timezone.now()
#    return f"{instance}/{time}+{filename}"

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    record_date = models.DateField(blank=True, null=True)
    image = ResizedImageField(size=[500,500], upload_to="record", blank=False)
    distance = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    pace_m = models.IntegerField(null=True, blank=True)
    pace_s = models.IntegerField(null=True, blank=True)
    time_h = models.IntegerField(null=True, blank=True)
    time_m = models.IntegerField(null=True, blank=True)
    time_s = models.IntegerField(null=True, blank=True)
    desc = models.TextField(blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)+ "_" + str(self.user) + "_" + str(self.record_date) + "_" + (str(self.title))