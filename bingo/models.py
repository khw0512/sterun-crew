from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField

# def image_upload_path(instance, filename):
#    time = timezone.now()
#    return f"{instance}/{time}+{filename}"

class BingoItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=100, blank=False, null=False)
    row = models.IntegerField(null=False, blank=False)
    col = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.content) + "_id_" + (str(self.item_id)) + "|" + str(self.row) + "_" + str(self.col) 
    
class BingoCheck(models.Model):
    bingo_item = models.ForeignKey(BingoItem, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + "_" + str(self.bingo_item) + "_" + str(self.completed)