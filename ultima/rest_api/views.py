from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet #adicionar viewset

from reserva.models import Reserva #Referenciar modelo
from rest_api.serializers import AgendamentoModelSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly #permissão apenas para leitura

class AgendamentoModelViewSet(ModelViewSet):
      queryset = Reserva.objects.all()
      serializer_class = AgendamentoModelSerializer
      authentication_classes = [TokenAuthentication]
      permission_classes = [IsAuthenticatedOrReadOnly]
      

#essa função sera acessada atrasves dos métodos get e post
@api_view(['GET', 'POST'])
def hello_word(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'Hello': 'World API'})

