from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reserva.models import Reserva
from rest_api.serializers import AgendamentoModelSerializer


class AgendamentoModelViewSet(ModelViewSet):
      queryset = Reserva.objects.all()
      serializer_class = AgendamentoModelSerializer
      

#essa função sera acessada atrasves dos métodos get e post
@api_view(['GET', 'POST'])
def hello_word(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'Hello': 'World API'})

