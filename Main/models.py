from django.db import models
from django.utils import timezone

# Create your models here.
class Train(models.Model):
    train_no = models.PositiveIntegerField(default=False)
    train_from = models.CharField(max_length=50)
    train_to = models.CharField(max_length=50)
    station1 = models.CharField(max_length=50, default=0)
    station2 = models.CharField(max_length=50, default=0)
    station3 = models.CharField(max_length=50, default=0)
    station4 = models.CharField(max_length=50, default=0)
    station5 = models.CharField(max_length=50, default=0)
    station6 = models.CharField(max_length=50, default=0)
    station7 = models.CharField(max_length=50, default=0)
    station8 = models.CharField(max_length=50, default=0)
    station9 = models.CharField(max_length=50, default=0)
    station10 = models.CharField(max_length=50, default=0)
    station11 = models.CharField(max_length=50, default=0)
    station12 = models.CharField(max_length=50, default=0)
    station13 = models.CharField(max_length=50, default=0)
    station14 = models.CharField(max_length=50, default=0)
    station15 = models.CharField(max_length=50, default=0)
    station16 = models.CharField(max_length=50, default=0)
    station17 = models.CharField(max_length=50, default=0)
    station18 = models.CharField(max_length=50, default=0)
    station19 = models.CharField(max_length=50, default=0)
    station20 = models.CharField(max_length=50, default=0)
    tarin_days = models.CharField(max_length=7)
    train_from_time = models.TimeField(default=timezone.now())
    train_to_time = models.TimeField(default=timezone.now())

class Station(models.Model):
    station_id = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    total_train = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
