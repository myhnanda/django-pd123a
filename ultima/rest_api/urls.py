from django.urls import path
from rest_api.views import hello_word, AgendamentoModelViewSet, PetshopModelViewSet, AvaliacaoViewSet

from rest_framework.routers import SimpleRouter


app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetshopModelViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('hello_world', hello_word, name= 'hello_world_api'),
]




urlpatterns += router.urls