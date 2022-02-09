from pyexpat import model
from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=50)
    # rating = models.IntegerField()
    desc = models.TextField()
    ip = models.CharField(max_length=50, unique=True)
    userAgent = models.CharField(max_length=250)
    time = models.DateTimeField(auto_now_add=True)
