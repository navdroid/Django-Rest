from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CarSerializer
from .serializers import EngineSerializer
from .models import Engine
from .models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('name')
    serializer_class = CarSerializer


class EngineViewSet(viewsets.ModelViewSet):
    queryset = Engine.objects.all().order_by('name')
    serializer_class = EngineSerializer
