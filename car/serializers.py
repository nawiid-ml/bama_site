from rest_framework.serializers import ModelSerializer, CharField
from .models import Car ,Sell_Car ,Price_Day

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields= '__all__'


class Sell_CarSerializer(ModelSerializer):
    class Meta:
        model = Sell_Car
        fields = '__all__'


class Price_DaySerializer(ModelSerializer):
    class Meta :
        model = Price_Day
        fields = '__all__'