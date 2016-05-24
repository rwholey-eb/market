from django.db import models

class Venues(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

class Organizers(models.Model):
    name = models.CharField(max_length=200)
