from rest_framework.serializers import ModelSerializer, CharField
from .models import Car ,Sell_Car ,Price_Day
from django.contrib.auth import get_user_model

User = get_user_model()
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

class UserSerializer(ModelSerializer):
    sell_car = Sell_CarSerializer(read_only=True,many=True)
    class Meta :
        model = User
        fields = '__all__'
