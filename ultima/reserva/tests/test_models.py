import pytest
from datetime import date
from model_bakery import baker
from reserva.models import PetShop, Reserva

#FIXTURE
@pytest.fixture
def reserva():
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        data_reserva=date.today(),
        turno = 'Tarde'
    )
    return reserva

@pytest.mark.django_db
def test_reserva_deve_retornar_string_formata(reserva): 
    assert str(reserva) == 'Tom: 2023-10-18 (Tarde)' # vc precisa alterar a data de acordo com o dia atual do seu computador

"""
@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    # data = date(2022, 10, 1)
    # reserva = baker.make(
    #     Reserva,
    #     nome='Tom',
    #     data=data,
    #     turno='Tarde'
    # )
    assert str(reserva) == 'Tom: 2022-10-01 - Tarde'

@pytest.mark.django_db
def test_petshop_qtd_reserva_deve_retornanr_numero_reservas():
    quantidade = 3
    petshop = baker.make(PetShop)
    baker.make(Reserva, _quantity=quantidade, petshop=petshop)

    assert petshop.qtd_reserva() == quantidade
"""