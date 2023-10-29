from django.core.management.base import BaseCommand, CommandParser
from reserva.models import PetShop
import random

#sorteat um codigo para sortear cliente

class Command(BaseCommand):
    def list_petshops(self):
        return PetShop.objects.all().values_list('pk', flat=True)

    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='How many persons should be participate in the contest'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help='Petshop ID to execute the contest'
        )

    def escolher_reserva(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        return random.sample(banhos_list, quantidade)
    
    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados do petshop que realizou o sorteio'
            )
        )
        self.stdout.write(f'Nome do Petshop: {petshop.nome}')
        self.stdout.write(
            f'Contato: {petshop.email}, {petshop.telefone}'
        )
    
    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados das pessoas e animais sorteados'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
                '='*35
            )
        )
        for reserva in reservas:
            self.stdout.write(
                f'Animal: {reserva.nome_pet}'
            )
            self.stdout.write(
                f'Tutor: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' *35
                )
            )




    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']


        petshop = PetShop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()

        banhos_escolhidos = self.escolher_reserva(reservas, quantity)

        for reserva in banhos_escolhidos:
            self.style.SUCCESS('Sorteio concluído')
        
        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)

