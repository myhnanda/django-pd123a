import pytest
from datetime import date
from model_bakery import baker
from reserva.models import Reserva, PetShop

@pytest.fixture
def reserva():
    data = date(2023, 10, 1)
    return baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='Tarde'
    )

@pytest.fixture
def petshop():
    return baker.make(PetShop)