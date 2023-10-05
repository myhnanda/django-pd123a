from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
from reserva.models import Reserva, PetShop


class AgendamentoPetshopSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class PetshopSerializer(ModelSerializer):
    
    reservas = AgendamentoPetshopSerializer(many=True)

    class Meta:
        model = PetShop
        fields = [
            'id',
            'nome',
            'email',
            'telefone',
            'reservas',
        ]
        

class PetshopNestedSerializer(ModelSerializer):

    class Meta:
        model = PetShop
        fields = [
            'id',
            'nome',
            'email',
            'telefone',
        ]



class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField): #é uma chave primaria de um relacionamento. 
    #quando eu quiser que na leitura ver os dados do pet mas na escrita não
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedSerializer
        super().__init__(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        dados = self.serializer(value, context = self.context).data
        return dados

class AgendamentoModelSerializer(ModelSerializer):

    #dados_petshop = SerializerMethodField() # não esta no banco de dados
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset = PetShop.objects.all(),
        read_only = False
     )  
    # def get_dados_petshop(self, obj):
    #     if obj.petshop is not None:
    #         serializer = PetshopNestedSerializer(instance=obj.petshop)
    #         return serializer.data
        
    class Meta:
        model = Reserva
        fields = '__all__'


