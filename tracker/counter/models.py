from django.db import models

class CounterNumber(models.Model):
    species = [
        ("Oree", "Oree"),
        ("Babawa", "Babawa"),
        ("Kinu", "Kinu"),
        ("Saku", "Saku")
    ]
    species = models.CharField(choices=species, max_length=200, unique=True, default="")
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.species