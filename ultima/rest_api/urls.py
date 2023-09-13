from django.urls import path
from rest_api.views import hello_word

app_name = 'rest_api'

urlpatterns = [
    path('hello_world', hello_word, name= 'hello_world_api'),
]
