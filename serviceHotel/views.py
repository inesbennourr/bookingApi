from django.shortcuts import render
from .models import * 
from .serializer import * 
from rest_framework import viewsets

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = ()
