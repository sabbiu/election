from __future__ import unicode_literals

from django.db import models




class Info(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateTimeField('date published')




# Create your models here.
