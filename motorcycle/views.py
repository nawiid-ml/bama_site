from django.http.response import HttpResponse , JsonResponse
from .models import Motorcycle , Sell_Motorcycle , Motorcycle_Price
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import Sell_MotorcycleSerializer , Motorcycle_PriceSerializer
from rest_framework import generics


class List_Motorcycle(generics.ListAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer


class Create_Motorcycle(generics.CreateAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class= Sell_MotorcycleSerializer  


class Update_Motorcycle(generics.UpdateAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer


class Delete_Motorcycle(generics.DestroyAPIView):
    Pk = Sell_Motorcycle.objects.get(pk=2)
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer(Pk)


class Retrieve_Motorcycle(generics.RetrieveAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer()


class View_Motorcycle(generics.ListCreateAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer


class View_Motorcycle_Price(generics.ListCreateAPIView):
    queryset = Motorcycle_Price.objects.all()
    serializer_class = Motorcycle_PriceSerializer



