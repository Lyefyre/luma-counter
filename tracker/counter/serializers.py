from rest_framework import serializers
from .models import CounterNumber

class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CounterNumber
        fields = ('value', 'description')