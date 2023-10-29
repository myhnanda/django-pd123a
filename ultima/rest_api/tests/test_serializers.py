import pytest
import datetime
from model_bakery import baker
from reserva.models import PetShop, Reserva, Avaliacao , CategoriaAnimal
from rest_api.serializers import AgendamentoModelSerializer
from rest_framework.test import APIClient
import reverse

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days= 1)
    petshop = baker.make(PetShop)
    categoria  = baker.make(CategoriaAnimal, nome = 'G')

    return {
        'nome': 'nome teste',
        'emaii': 'email@email.com',
        'nome_pet': 'pet teste',
        'data_reserva': ontem,
        'turno': 'manhã',
        'porte': 0,
        'observacoes': '',
        'petshop': petshop.pk,
        'categoria': categoria.pk
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data= dados_agendamento_errado)
    assert not serializer.is_valid()

