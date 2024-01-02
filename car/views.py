from django.http.response import HttpResponse, JsonResponse
from .models import Car ,Sell_Car ,Price_Day
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import Sell_CarSerializer,Price_DaySerializer
from rest_framework import generics



class CarList(generics.ListAPIView):
    queryset = Sell_Car.objects.all()
    serializer_class = Sell_CarSerializer



class Create_Car(generics.CreateAPIView):
    queryset = Sell_Car.objects.all()
    serializer_class=Sell_CarSerializer



class Update_Car(generics.UpdateAPIView):
    queryset = Sell_Car.objects.all().order_by('id')
    serializer_class=Sell_CarSerializer


class Delete_Car(generics.DestroyAPIView):
    queryset = Sell_Car.objects.all()
    serializer_class=Sell_CarSerializer


class Retrieve_Car(generics.RetrieveAPIView):
    queryset = Sell_Car.objects.all()
    serializer_class=Sell_CarSerializer


class View_Car(generics.ListCreateAPIView):
    queryset = Sell_Car.objects.all()
    serializer_class = Sell_CarSerializer


class View_Price(generics.ListAPIView):
    queryset =Price_Day.objects.all()
    serializer_class = Price_DaySerializer


class Create_Price_Car(generics.CreateAPIView):
    queryset = Price_Day.objects.all()
    serializer_class =Price_DaySerializer    


    

