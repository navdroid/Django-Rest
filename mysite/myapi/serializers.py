# serializers.py
from rest_framework import serializers

from .models import Car
from .models import Engine


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'car'
        model = Car
        fields = ('name', 'year')


class EngineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'engine'
        model = Engine
        fields = ('name', 'power')
