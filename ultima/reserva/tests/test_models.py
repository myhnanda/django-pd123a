import pytest
from datetime import date
from model_bakery import baker
from reserva.models import PetShop, Reserva, CategoriaAnimal, Avaliacao
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.validators import MaxValueValidator, MinValueValidator

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
def test_reserva_deve_retornar_string_formatada(reserva): 
    assert str(reserva) == 'Tom: 2023-10-27 (Tarde)' # vc precisa alterar a data de acordo com o dia atual do seu computador



@pytest.mark.django_db
def test_categoria_animal():
    cachorro = CategoriaAnimal(nome = 'C')
    gato = CategoriaAnimal(nome = 'G')

    assert str(cachorro) == 'Cachorro'
    assert str(gato) == 'Gato'


@pytest.mark.django_db
def test_petshop():
    petshop = baker.make(
        PetShop,
        nome = 'Pets',
        email = 'petsshop@gmail.com',
        telefone = '1234456778'
    )

    assert str(petshop) == 'Pets: petsshop@gmail.com - 1234456778'



@pytest.mark.django_db
def test_avaliacao_nota_valida():

    petshop = PetShop.objects.create(nome="PetShop Teste")
    
    # Testar uma nota válida
    avaliacao = Avaliacao(petshop= petshop, nota=5, comentario="Bom serviço")
    avaliacao.full_clean() 

@pytest.mark.django_db
def test_nota_mínima():
    petshop = PetShop.objects.create(nome="PetShop Teste")

    avaliacao = Avaliacao(petshop = petshop, nota = 0, comentario="Nota mínima")
    avaliacao.full_clean()

@pytest.mark.django_db
def test_nota_máxima():
    petshop = PetShop.objects.create(nome="PetShop Teste")

    avaliacao = Avaliacao(petshop = petshop, nota = 10, comentario="Nota máxima")
    avaliacao.full_clean()


@pytest.mark.django_db
def test_nota_invalida():
    petshop = PetShop.objects.create(nome="PetShop Teste")

    avaliacao = Avaliacao(petshop = petshop, nota = 11, comentario="A nota deve ser no máximo 10")
    avaliacao.full_clean()




    



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