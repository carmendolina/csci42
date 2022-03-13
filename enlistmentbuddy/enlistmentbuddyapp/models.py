from django.db import models
from django.urls import reverse

# Create your models here.


class IndexCard(models.Model):
    code = models.CharField(max_length=20, null=True)
    section = models.CharField(max_length=20, null=True)
    sched = models.CharField(max_length=10, null=True)
    #start = models.CharField(max_length=10, null=True)
    #end = models.CharField(max_length=10, null=True)
    start = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    venue = models.CharField(max_length=20, null=True)
    professor = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} {} {}-{}'.format(self.code, self.section, self.start, self.end)