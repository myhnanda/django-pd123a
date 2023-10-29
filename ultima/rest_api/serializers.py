from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
from reserva.models import Reserva, PetShop, Avaliacao, CategoriaAnimal
import datetime

class CategoriaAnimalSerializer(ModelSerializer):
    class Meta:
        model = CategoriaAnimal
        fields = '__all__'

class AgendamentoPetshopSerializer(ModelSerializer):
    categoria = CategoriaAnimalSerializer()
    class Meta:
        model = Reserva
        fields = '__all__'


class PetshopSerializer(ModelSerializer):
    
        reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )
        
        class Meta:
            model = PetShop
            fields = '__all__'
        
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
    
class PetshopNestedSerializer(ModelSerializer):

    class Meta:
        model = PetShop
        fields = '__all__'



class AgendamentoModelSerializer(ModelSerializer):

    def validate_data(self, value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Não é possivel realizar um agendamento para o passado')
        return value
    
    class Meta:
        model = Reserva
        fields = '__all__'
        
class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
