from django.db import models

# Create your models here.
#Classe de reserva de horário de banho do pet
class Reserva(models.Model):
    #na hora que ele vai escolher a data ter opções (fazer seleção)
    PORTE_OPCOES = (
        (0,'Pequeno'),
        (1,'Médio'),
        (2,'Grande')
    )
    #turnos para reserva
    TURNOS_OPCOES = (
        ('manhã','Manhã'),
        ('tarde', 'Tarde')
    )

    #informações do usuário
    nome = models.CharField(max_length=150)
    email = models.EmailField()

    #informações do pet
    nome_pet = models.CharField(max_length=50)
    porte = models.CharField(choices= PORTE_OPCOES, max_length=120)

    #informações da reserva
    data_reserva = models.DateField(help_text='Ultilize o formato dd/mm/aaaa')
    turno = models.CharField(choices = TURNOS_OPCOES, max_length=120)

    #   Observações 
    observacoes = models.TextField(verbose_name= 'Observações', max_length=3000, blank=True)


    def __str__(self):
        return f'{self.nome}: {self.data_reserva} ({self.turno})'

    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de banho'

    