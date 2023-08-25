from django.db import models


# Create your models here.

#SQL BANCO DE DAODS

#modelo é uma classe em python, com os atributos (campos) que queremos

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.CharField(max_length= 3000)
    data = models.DateField(auto_now_add=True)
    lido = models.BooleanField(verbose_name= 'Mensagem lida', default=False)

#STRING PADRÃO PARA ADMIN
    def __str__(self) -> str:
        return f'{self.nome} - {self.email}'
    
    class Meta: 
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contato'
        ordering = ['-data', 'lido']
        
    

class Reserva(models.Model):
    nome_pet = models.CharField(max_length= 50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacoes = models.CharField(max_length= 2000)
