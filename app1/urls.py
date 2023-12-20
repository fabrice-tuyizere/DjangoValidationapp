
from django.urls import path
from .views import create_person, success_page, create_vehicle

urlpatterns = [
    path('', create_person, name='create_person'),
     path('createvehicle/', create_vehicle, name='create_vehicle'),
    path('success/', success_page, name='success_page'),
]
