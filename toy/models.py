from django.db import models
from django.contrib.gis.db.models import GeometryField


class Toy(models.Model):
    title = models.CharField(max_length=128)
    description = models.SlugField()
    location = GeometryField(srid=4326)

    def __str__(self):
        return self.title