from django.db import models

class Venues(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def save(self, *args, **kwargs):
        try:
            self.capacity = int(self.capacity)
        except ValueError:
            self.capacity = 0
        super(Venues, self).save(*args, **kwargs)

class Organizers(models.Model):
    name = models.CharField(max_length=200)
