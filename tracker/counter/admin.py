from django.contrib import admin
from .models import *

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SpeciesModel, SpeciesAdmin)

class CounterAdmin(admin.ModelAdmin):
    list_display = [
        'species',
        'value'
    ]

admin.site.register(CounterNumber, CounterAdmin)
