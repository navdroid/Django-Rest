from django.db import models

# Create your models here.
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=60)
    year = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=60)
    power = models.FloatField(null=False, blank=False, default=None)
