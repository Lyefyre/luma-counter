from django.db import models

class TemtemName(models.Model):
    species = [
        ("Oree", "Oree"),
        ("Babawa", "Babawa")
    ]
    name = models.CharField(choices=species, max_length=200)
    placeholder = models.CharField(max_length=200, default="Placeholder")

    def __str__(self):
        return self.name

class CounterNumber(models.Model):
    value = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description