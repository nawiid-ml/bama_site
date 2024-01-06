from django.contrib.admin import ModelAdmin,register
from .models import Truck ,Sell_Truck


@register(Truck)
class Truck_Admin(ModelAdmin):
    search_fields = ['brand']

@register(Sell_Truck)
class Sell_Truck(ModelAdmin):
    list_display=('brand','model', 'price')
