from django.urls import path
from .views import (List_truck , Create_SellTruck,
                    Update_sellTruck,Delete_SellTruck,
                    Retrieve_SellTruck,)
urlpatterns = [
    path('truck',List_truck.as_view(),name='truck'),
    path('sell_truck',Create_SellTruck.as_view(),name='sell_truck'),
    path('update_selltruck',Update_sellTruck.as_view(),name='update_selltruck'),
    path('delete_selltruck',Delete_SellTruck.as_view(),name='delete_selltruck'),
    path('retrieve_selltruck',Retrieve_SellTruck.as_view,name='retrieve_selltruck'),
]
