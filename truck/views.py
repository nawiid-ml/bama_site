from .models import Sell_Truck 
#from django.shortcuts import render
from .serializers import SellTruckSerializer ,  UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


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


class User_List(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
