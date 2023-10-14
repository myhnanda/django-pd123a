from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
from reserva.models import Reserva, PetShop, Avaliacao, CategoriaAnimal

class CategoriaAnimalSerializer(ModelSerializer):
    class Meta:
        model = CategoriaAnimal
        fields = '__all__'

class AgendamentoPetshopSerializer(ModelSerializer):
    categoria = CategoriaAnimalSerializer()
    class Meta:
        model = Reserva
        fields = ['id',
                  'nome',
                  'email',
                  'nome_pet',
                  'data_reserva',
                  'turno',
                  'porte',
                  'observacoes'
        ]


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
        
class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField): #é uma chave primaria de um relacionamento. 
    #quando eu quiser que na leitura ver os dados do pet mas na escrita não
    def _init_(self, **kwargs):
        self.serializer = PetshopNestedSerializer
        super()._init_(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        dados = self.serializer(value, context = self.context).data
        return dados
    
class PetshopNestedSerializer(ModelSerializer):

    class Meta:
        model = PetShop
        fields = '__all__'




class AgendamentoModelSerializer(ModelSerializer):

    dados_petshop = SerializerMethodField() # não esta no banco de dados
    #petshop = PetShopRelatedFieldCustomSerializer(
        # queryset = PetShop.objects.all(),
        # read_only = False)
 
    def get_dados_petshop(self, obj):

        if obj.petshop is not None:
            serializer = PetshopNestedSerializer(instance=obj.petshop)
            return serializer.data
        
    class Meta:
        model = Reserva
        fields = '__all__'
        
class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
