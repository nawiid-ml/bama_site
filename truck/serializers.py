from rest_framework.serializers import ModelSerializer, CharField
from .models import Sell_Truck , Truck


class SellTruckSerializer(ModelSerializer):
    class Meta:
        model = Sell_Truck
        fields = '__all__'


class TruckSerializer(ModelSerializer):
    class Meta:
        model = Truck
        fields ='__search__'
