from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SpeciesModel(models.Model):
    name = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='media', default="")
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(150, 150)], format='PNG', options={'quality': 70})

    def __str__(self):
        return self.name

class CounterNumber(models.Model):
    species = models.ForeignKey(SpeciesModel, related_name="CounterNumber", on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.species.name