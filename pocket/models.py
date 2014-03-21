import random
from django.db import models

# Create your models here.


class PocketGenerator(models.Manager):
    def create_pocket(self, number):
        number = self.create(number=number)
        return number


class Pocket(models.Model):
    number = models.CharField(max_length=1)
    objects = PocketGenerator()

    def __unicode__(self):
        return self.number










