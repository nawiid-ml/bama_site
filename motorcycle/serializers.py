from rest_framework.serializers import ModelSerializer, CharField
from .models import Motorcycle , Sell_Motorcycle,Motorcycle_Price


class MotorcycleSerializer(ModelSerializer):
    class Meta:
       model = Motorcycle
       fields = '__all__'

class Sell_MotorcycleSerializer(ModelSerializer):
    class Meta:
        model = Sell_Motorcycle 
        fields = '__all__'


class Motorcycle_PriceSerializer(ModelSerializer):
    class Meta:
        model = Motorcycle_Price
        fields ='__all__'     