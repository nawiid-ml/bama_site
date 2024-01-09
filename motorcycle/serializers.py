from rest_framework.serializers import ModelSerializer, CharField
from .models import Motorcycle , Sell_Motorcycle,Motorcycle_Price
from django.contrib.auth import get_user_model

User = get_user_model()


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
        fields = '__all__'     

class UserSerializer(ModelSerializer):
    sell_motorcycle = Sell_MotorcycleSerializer (read_only =True ,many=True)
    class Meta :
        model = User
        fields = '__all__'