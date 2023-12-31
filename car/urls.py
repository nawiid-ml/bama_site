from django.urls import path
from .views import (CarList, Create_Car,
                    Update_Car,Delete_Car,
                    Retrieve_Car,View_Car,
                    View_Price,Create_Price_Car,
                    Users_List)

urlpatterns = [
    path('car',CarList.as_view(),name='car_list'),
    path('sell_car',Create_Car.as_view(),name='sell_car'),
    path('update_sell_car/<int:pk>',Update_Car.as_view(),name='sell_car_update'),
    path('delete_car/<int:pk>',Delete_Car.as_view(),name='delete_car'),
    path('retrieve_car/int:pk',Retrieve_Car.as_view(),name='car_retrieve'),
    path('view_car',View_Car.as_view(),name='view_car'),
    path('price',View_Price.as_view(),name='price'),
    path('create_price',Create_Price_Car.as_view(),name='create_price'),
    path('users/',Users_List.as_view(),name='users')
]
