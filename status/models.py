from django.db import models

# Create your models here.
class Schedule(models.Model):
    hour = models.IntegerField()
    minutes = models.IntegerField()
    duration = models.IntegerField()
    

class Status(models.Model):
    status = models.BooleanField()