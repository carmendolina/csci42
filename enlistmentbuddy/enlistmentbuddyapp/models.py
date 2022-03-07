from django.db import models
from django.urls import reverse

# Create your models here.


class IndexCard(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=5)
    age = models.IntegerField()