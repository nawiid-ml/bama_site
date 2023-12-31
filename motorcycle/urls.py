from django.urls import path
from .views import list_1
urlpatterns = [
    path('list',list_1,name='')
]
