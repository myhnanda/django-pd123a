import  pytest
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Reserva, PetShop, Avaliacao, CategoriaAnimal
from rest_api.serializers import PetshopSerializer, AgendamentoModelSerializer
import datetime
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db


@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    assert len(resposta.data['results']) == 1


@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(PetShop)
    categoria  = baker.make(CategoriaAnimal, nome = 'G')
    return {
        "nome": "Juliana",
        "email": "juliana@gmail.com",
        "nome_pet": "Nabuco",
        "porte": 0,
        "data_reserva": "2023-10-29",
        "turno": "tarde",
        "observacoes": "agitado",
        "petshop": petshop.pk,
        "categoria": categoria.pk
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201
#VERFICA SE FOI CRIANDO CORRETAMENTE NO BANCO DE DADOS
    agendamento_criado = Reserva.objects.get(nome="Juliana")
    assert agendamento_criado is not None
    assert agendamento_criado.nome_pet == "Nabuco"
    assert agendamento_criado.data_reserva == datetime.date(2023, 10, 29)


@pytest.mark.django_db
def test_consultar_agendamento_especifico(agendamento, dados_agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento/1', dados_agendamento)
    assert resposta.status_code == 200
    assert resposta.data['nome'] ==  agendamento.nome

@pytest.mark.django_db
def test_atualizar_agendamento_especifico(agendamento, usuario):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.patch('/api/agendamento/1', {'nome': 'reserva teste atualizada'})
    assert resposta.status_code == 200
    assert resposta.data['nome'] == 'reserva teste atualizada' and resposta.data['nome_pet'] == agendamento.nome_pet

@pytest.mark.django_db
def test_remover_agendamento_especifico(agendamento, usuario):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.delete('/api/agendamento/1')
    assert resposta.status_code == 204
    assert len(cliente.get('/api/agendamento').data['results']) == 0