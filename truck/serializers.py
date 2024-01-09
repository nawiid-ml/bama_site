from rest_framework.serializers import ModelSerializer
from .models import Sell_Truck , Truck
from django.contrib.auth import get_user_model

User = get_user_model()


class SellTruckSerializer(ModelSerializer):
    class Meta:
        model = Sell_Truck
        fields = '__all__'


class TruckSerializer(ModelSerializer):
    class Meta:
        model = Truck
        fields ='__search__'


class UserSerializer(ModelSerializer):
    sell_truck = SellTruckSerializer(read_only=True , many=True)
    class Meta :
        model = User
        fields = '__all__'