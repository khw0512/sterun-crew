from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField
from django.db.models import UniqueConstraint

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

    def delete(self, *args, **kwargs):
        # 실제 파일 삭제
        if self.image:
            self.image.delete(save=False)
        # DB 데이터 삭제
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.confirmed)+ "_" + str(self.user) + "_" + str(self.record_date) + "_" + (str(self.title))


class PersonalRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', '심사중'),
        ('verified', '인증됨'),
        ('rejected', '반려됨'),
    ]
    CATEGORY_CHOICES = [
        ('10K', '10km'),
        ('HM', '하프마라톤'),
        ('FM', '풀마라톤'),
    ]
    event_name = models.CharField(max_length=50)
    runner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    date = models.DateField(blank=True, null=True)
    record = models.DurationField()  # 시간 기록
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    evidence_url = ResizedImageField(size=[500,500], upload_to="record", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(blank=True)

    def delete(self, *args, **kwargs):
        # 실제 파일 삭제
        if self.evidence_url:
            self.evidence_url.delete(save=False)
        # DB 데이터 삭제
        super().delete(*args, **kwargs)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['runner', 'category'], name='unique_user_category')
        ]

    def __str__(self):
        return f"{self.runner} - {self.category}: {self.record}"

class Team(models.Model):
    STATUS_CHOICES = [
        ('ready', '준비중'),
        ('go', '운영중'),
        ('stop', '완료'),
    ]
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ready')
    def __str__(self):
        return str(self.team_name)

class TeamMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    leader = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='uunique_user_only_one_team')
        ]

    def __str__(self):
        return str(self.team)+"_"+str(self.user)