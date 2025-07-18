from django.db import models
from django.utils import timezone
# Create your models here.
class Schedule(models.Model):
    # hour = models.IntegerField()
    # minutes = models.IntegerField()
    # duration = models.IntegerField()
    start_datetime = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=0)
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    

class Status(models.Model):
    status = models.BooleanField()