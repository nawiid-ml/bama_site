from django.contrib.admin import ModelAdmin,register
from .models import Car,Sell_Car,Price_Day


@register(Car)
class Car_Admin(ModelAdmin):
    pass


@register(Sell_Car)
class Sell_Car_Admin(ModelAdmin):
    pass

@register(Price_Day)
class Price_Day_Admin(ModelAdmin):
    pass
