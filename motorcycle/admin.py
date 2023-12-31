from django.contrib.admin import ModelAdmin,register
from .models import Motorcycle,Sell_Motorcycle,Motorcycle_Price

@register(Motorcycle)
class Motorcycle_Admin(ModelAdmin):
    pass

@register(Sell_Motorcycle)
class Sell_Motorcycle_Admin(ModelAdmin):
    pass

@register(Motorcycle_Price)
class Motorcycle_price(ModelAdmin):
    pass


