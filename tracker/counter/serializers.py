from rest_framework import serializers
from .models import CounterNumber, SpeciesModel, Account
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User

class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    image_small = serializers.ImageField(read_only=True)
    class Meta:
        model = SpeciesModel
        fields = ['name', 'id', 'image_small']

class NumberSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    species = SpeciesSerializer(many=False, read_only=False)
    class Meta:
        model = CounterNumber
        fields = ['species', 'value', 'id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = [
            'username',
            'id'
        ]
        fields = [
            'username',
            'name'
        ]

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Account
        read_only_fields = [
            'user'
        ]
        fields = [
            'user'
        ]
        