import pytest

from pytest_django.asserts import assertContains

from model_bakery import baker

from datetime import date, timedelta

from reserva.models import Reserva, PetShop

from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    resposta = client.get('/reserva/criar/')
    assert resposta.status_code == 200
    assertTemplateUsed(resposta, 'criar_reserva.html')

@pytest.mark.django_db
def test_criar_reserva_deve_funcionar(client):
    petshop = baker.make(PetShop)
    dados = {
        "nome": "teste",
        "email": "email@teste.com",
        "nome_pet": "teste pet",
        "data_reserva": date.today().strftime("%d/%m/%Y"),
        "turno": "tarde",
        "porte": 1,
        "petshop": petshop.id,
        "observacoes": ""
    }
    resposta = client.post("/reserva/criar/", dados)
    assert resposta.status_code == 200
    assert Reserva.objects.count() > 0


@pytest.mark.django_db
def test_criar_reserva_nao_deve_funcionar(client):
    petshop = baker.make(PetShop)
    dados = {
        "nome": "teste",
        "email": "email@teste.com",
        "nome_pet": "teste pet",
        "data": date.today().strftime("%d/%m/%Y"),
        "turno": "noite",
        "turno": 1,
        "petshop": petshop.id,
        "observacoes": ""
    }
    resposta = client.post("/reserva/criar/", dados)
    assert resposta.status_code == 200
    assert Reserva.objects.count() == 0
'''
@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client):
    amanha = date.today() + timedelta(days = 1)
    dados = {
        'nome':'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'turno':'tarde',
        'porte': '0',
        'observacoes': 'ele ta bem fedido'
    }
    response = client.post('/reserva/criar/', dados)

    assert response.status_code == 200
    assert 'Sua reserva doi registrada com sucesso!' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client):
    amanha = date.today() + timedelta(days = 1)
    dados = {
        'nome':'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'turno':'tarde',
        'porte': '0',
        'observacoes': 'ele ta bem fedido'
    }
    response = client.post('/reserva/criar/', dados)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados['nome']
    assert reserva.nome_pet == dados['nome_pet']

'''

#dados duplicados agora melhorar usando fixture
@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days = 1)
    dados = {
        'nome':'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'turno':'tarde',
        'porte': '0',
        'observacoes': 'ele ta bem fedido'
    }
    return dados

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):
    response = client.post('/reserva/criar/', dados_validos)

    assert response.status_code == 200
    assert 'Sua reserva doi registrada com sucesso!' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
     response = client.post('/reserva/criar/', dados_validos)
     
     assert Reserva.objects.all().count() == 1
     reserva = Reserva.objects.first()

     assert reserva.nome == dados_validos['nome']
     assert reserva.nome_pet == dados_validos['nome_pet']
