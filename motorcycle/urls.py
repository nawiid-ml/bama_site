from django.urls import path
from .views import (List_Motorcycle , Create_Motorcycle,
                    Update_Motorcycle , Delete_Motorcycle,
                    Retrieve_Motorcycle , View_Motorcycle,
                    View_Motorcycle_Price)
urlpatterns = [
    path('motorcycle',List_Motorcycle.as_view(),name='motorcycle'),
    path('sell_motorcycle',Create_Motorcycle.as_view(),name='sell_motorcycle'),
    path('update_motorcycle',Update_Motorcycle.as_view(),name="update_motorcycle"),
    path('delete_motorcycle/<int:pk>',Delete_Motorcycle.as_view(),name='delete_motorcycle'),
    path('retrieve_motorcycle',Retrieve_Motorcycle.as_view(),name='retrieve_motorcycle'),
    path('view_motorcycle',View_Motorcycle.as_view(),name='view_motorcycle'),
    path('motorcycle_price',View_Motorcycle_Price.as_view(),name='motorcycle_price')
]
