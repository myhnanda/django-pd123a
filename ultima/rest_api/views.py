from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet #adicionar viewset

from reserva.models import Reserva, PetShop, Avaliacao, CategoriaAnimal #Referenciar modelo
from rest_api.serializers import AgendamentoModelSerializer, PetshopSerializer, AvaliacaoSerializer, CategoriaAnimalSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly #permissão apenas para leitura



class AgendamentoModelViewSet(ModelViewSet):
      queryset = Reserva.objects.all()
      serializer_class = AgendamentoModelSerializer      
      permission_classes = [IsAuthenticatedOrReadOnly]
      authentication_classes = [TokenAuthentication]
      def perform_destroy(self, instance):
        # Esta função é chamada para executar a remoção de um objeto
        instance.delete()
        
class PetshopModelViewSet(ModelViewSet):
     queryset = PetShop.objects.all()
     serializer_class = PetshopSerializer
     permission_classes = [IsAuthenticatedOrReadOnly]
     authentication_classes = [TokenAuthentication]

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication]


class CategoriaAnimalViewSet(ModelViewSet):
    queryset = CategoriaAnimal.objects.all()
    serializer_class = CategoriaAnimalSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]


    
#essa função sera acessada atrasves dos métodos get e post
@api_view(['GET', 'POST'])
def hello_word(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'Hello': 'World API'})




     



     




