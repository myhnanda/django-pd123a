from datetime import date, timedelta
import pytest
from reserva.forms import ReservaForm
from reserva.models import Reserva

@pytest.mark.django_db
def test_data_resevera_no_passado():
    data_reserva = date(2022,1,1)    #data no passado
    form_data = {
        'nome': 'João da Silva',
        'email': 'joao@example.com',
        'nome_pet': 'Totó',
        'data_reserva': data_reserva,
        'turno': 'manha',
        'porte': 'pequeno',
        'observacoes': 'Nenhuma observação',
    }

    form = ReservaForm(data= form_data)
    assert not form.is_valid()
    assert 'data_reserva' in form.errors
    assert form.errors['data_reserva'][0] == 'Não é possível reservar o banho para a data no passado. Tente outra data'

@pytest.mark.django_db
def test_formulario_reserva_com_muitas_reservas():
   for _ in range(4):
        Reserva.objects.create(
            nome='João da Silva',
            email='joao@example.com',
            nome_pet='Totó',
            data_reserva=date.today(),
            turno='manhã',
            porte=0,
            observacoes='Nenhuma observação',
        )
   data = {
        'nome': 'João da Silva',
        'email': 'joao@example.com',
        'nome_pet': 'Totó',
        'data_reserva': date.today(),
        'turno': 'manhã',  # Escolha válida
        'porte': 0,
        'observacoes': 'Nenhuma observação',
    }
   
   form = ReservaForm(data) 
   assert not form.is_valid()
   assert 'data_reserva' in form.errors
   assert form.errors['data_reserva'][0] == 'Já existem mais de 4 reservas para essa data e período! Tente outra data e período!'


@pytest.mark.django_db
def test_formulario_reserva_valido():
    data = {
        'nome': 'João da Silva',
        'email': 'joao@example.com',
        'nome_pet': 'Totó',
        'data_reserva': date.today(),
        'turno': 'manhã',
        'porte': '0',
        'observacoes': 'Nenhuma observação',
    }
    form = ReservaForm(data)
    assert form.is_valid()