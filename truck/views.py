from django.http.response import HttpResponse , JsonResponse
from .models import Sell_Truck , Truck
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import SellTruckSerializer , TruckSerializer
from rest_framework import generics


class List_truck (generics.ListAPIView):
    queryset = Sell_Truck.objects.all()
    serializer_class = SellTruckSerializer


class Create_SellTruck(generics.CreateAPIView):
    queryset = Sell_Truck.objects.all()
    serializer_class = SellTruckSerializer

class Update_sellTruck (generics.UpdateAPIView):
    queryset = Sell_Truck.objects.all()
    serializer_class = SellTruckSerializer


class Delete_SellTruck(generics.DestroyAPIView):
    queryset=Sell_Truck.objects.all()
    serializer_class=SellTruckSerializer


class Retrieve_SellTruck(generics.RetrieveAPIView):
    queryset = Sell_Truck.objects.all()
    serializer_class = SellTruckSerializer
