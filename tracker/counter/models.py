from django.db import models

class CounterNumber(models.Model):
    value = models.IntegerField(),
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description