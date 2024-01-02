from django.contrib.admin import ModelAdmin,register
from .models import Motorcycle,Sell_Motorcycle,Motorcycle_Price

@register(Motorcycle)
class Motorcycle_Admin(ModelAdmin):
    search_fields =['brand']

@register(Sell_Motorcycle)
class Sell_Motorcycle_Admin(ModelAdmin):
    list_display=('brand','model')
    

@register(Motorcycle_Price)
class Motorcycle_price(ModelAdmin):
    list_display = ['brand','model','price']


