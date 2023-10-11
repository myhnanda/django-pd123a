import pytest

from pytest_django.asserts import assertContains

from model_bakery import baker

from datetime import date

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
