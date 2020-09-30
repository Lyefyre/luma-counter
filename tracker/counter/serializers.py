from rest_framework import serializers
from .models import CounterNumber, SpeciesModel

class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    image_small = serializers.ImageField(read_only=True)
    class Meta:
        model = SpeciesModel
        fields = ['name', 'id', 'image_small']

class NumberSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer(many=False, read_only=False)
    class Meta:
        model = CounterNumber
        fields = ['species', 'value']
        