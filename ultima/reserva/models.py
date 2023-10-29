from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoriaAnimal(models.Model):
    CATEGORIA_CHOICES = (
        ('C', 'Cachorro'),
        ('G', 'Gato')
    )
    nome = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.get_nome_display()

    
class PetShop(models.Model):
    nome = models.CharField('Nome',max_length=50)
    email = models.EmailField('E-mail', blank= True)
    telefone = models.CharField('Telefone', max_length=20)


    def __str__(self):
        return f'{self.nome}: {self.email} - {self.telefone}'
    
    def qtd_reserva(self):
        return self.reservas.count()
    
    class Meta:
        verbose_name = 'Petshop'
        verbose_name_plural = 'Petshops'
        ordering = ['nome']

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
    porte =models.IntegerField(choices = PORTE_OPCOES, null=True, blank=True)
    #informações da reserva
    data_reserva = models.DateField(help_text='Ultilize o formato dd/mm/aaaa', null=True, blank = True)
    turno = models.CharField(choices = TURNOS_OPCOES, max_length=120, blank = True)
    #   Observações 
    observacoes = models.TextField(verbose_name= 'Observações', max_length=3000, blank=True)
    petshop = models.ForeignKey(PetShop, models.SET_NULL, null=True, related_name='reservas')
    categoria = models.ForeignKey(CategoriaAnimal, models.SET_NULL, null=True, related_name='reservas')
    
    def __str__(self):
        return f'{self.nome}: {self.data_reserva} ({self.turno})'

    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de banho'
        ordering = ['nome', 'email','nome_pet', 'porte', 'data_reserva','turno', 'observacoes', 'petshop', 'categoria']

class Avaliacao(models.Model):
    petshop = models.ForeignKey(PetShop, on_delete=models.CASCADE)
    nota = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0, "A nota deve ser no mínimo 0."),
            MaxValueValidator(10, "A nota deve ser no máximo 10.")
        ]
    )
    comentario = models.TextField()

    def __str__(self):
        return f'Avaliação de {self.nota} para {self.petshop}'



