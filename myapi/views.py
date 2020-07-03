from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.order_by('name')
    serializer_class = HeroSerializer