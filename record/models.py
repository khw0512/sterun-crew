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


class PersonalRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', '심사 중'),
        ('verified', '인증됨'),
        ('rejected', '반려됨'),
    ]
    CATEGORY_CHOICES = [
        ('10K', '10km'),
        ('HM', 'Half Marathon'),
        ('FM', 'Full Marathon'),
    ]
    runner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    record = models.DurationField()  # 시간 기록
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    evidence_url = ResizedImageField(size=[500,500], upload_to="record", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('runner', 'category')  # 한 종목에 1개 PR

    def __str__(self):
        return f"{self.runner} - {self.category}: {self.record}"
