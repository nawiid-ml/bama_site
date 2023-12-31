from django.contrib.admin import ModelAdmin,register
from .models import Truck ,Sell_Truck
# Register your models here.

@register(Truck)
class Truck_Admin(ModelAdmin):
    pass

@register(Sell_Truck)
class Sell_Truck(ModelAdmin):
    pass
