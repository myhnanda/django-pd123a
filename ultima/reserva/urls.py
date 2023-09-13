from django.urls import path

from reserva.views import *

# app_name = 'reserva' #utlizado para criar um name space


urlpatterns = [
    path('reserva/', criar_reserva, name = 'criar_reserva'),
    
]
