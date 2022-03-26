from django.db import models


class Location(models.Model):
    name=models.CharField(max_length=50)

# Create your models here.
