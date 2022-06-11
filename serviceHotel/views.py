from django.shortcuts import render
from .models import * 
from .serializer import * 
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = ()


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]    
    filter_fields =  ['hotel']
    permission_classes = ()
