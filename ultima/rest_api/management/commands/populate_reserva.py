from typing import Any
from model_bakery import baker
from django.core.management.base import BaseCommand
from reserva.models import Reserva 

class Command(BaseCommand):
    help = 'Comando para criar dados aleatorios'

    def handle(self, *args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'Criando {total} dados aleatorios')
        )

        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()

        self.stdout.write(
            self.style.SUCCESS('tudo pronto!')
        )

