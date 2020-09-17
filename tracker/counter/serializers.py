from rest_framework import serializers
from .models import CounterNumber, TemtemName

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CounterNumber
        fields = ('value', 'description')

class TemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemtemName
        fields = ('name', 'placeholder')