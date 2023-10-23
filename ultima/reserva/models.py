from django.db import models


class CategoriaAnimal(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class PetShop(models.Model):
    nome = models.CharField('Nome',max_length=50)
    email = models.EmailField('E-mail', blank= True)
    telefone = models.CharField('Telefone', max_length=20)
   
    def __str__(self):
        return super().__str__()
    
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


class Avaliacao(models.Model):
    petshop = models.ForeignKey(PetShop, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return super().__str__()
    
#from django.db import models  <-- você não pode importar biblioteca no final do código, sempre no inicio


