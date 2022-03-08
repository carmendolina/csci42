from django.db import models
from django.urls import reverse

# Create your models here.


class IndexCard(models.Model):
    code = models.CharField(max_length=20, null=True)
    section = models.CharField(max_length=20, null=True)
    venue = models.CharField(max_length=20, null=True)
    professor = models.CharField(max_length=50, null=True)