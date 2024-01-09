from .models import  Sell_Motorcycle , Motorcycle_Price
#from django.shortcuts import render
from .serializers import Sell_MotorcycleSerializer , Motorcycle_PriceSerializer , UserSerializer 
from rest_framework import generics
from django.contrib.auth import get_user_model


User = get_user_model()


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
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer()


class Retrieve_Motorcycle(generics.RetrieveAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer()

    


class View_Motorcycle(generics.ListCreateAPIView):
    queryset = Sell_Motorcycle.objects.all()
    serializer_class = Sell_MotorcycleSerializer


class View_Motorcycle_Price(generics.ListCreateAPIView):
    queryset = Motorcycle_Price.objects.all()
    serializer_class = Motorcycle_PriceSerializer


class User_List(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer