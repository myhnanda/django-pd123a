from django import forms
from base.models import Contato, Reserva

# Formulario contato
class ContatoForm(forms.ModelForm):
    #meta dados do formulario
    class Meta: 
        #definir modelo base
        model = Contato

        #definir quais os campos do formulário
        fields = ['nome', 'email', 'mensagem']

        #definir os widgets 
        widgets = {
            'nome': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira o seu nome aqui'
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu e-mail aqui'
                }
            ), 
            'mensagem': forms.TextInput(
                attrs={
                    'placeholder': 'Digite sua mensagem aqui'
                }
            )
        }

        #definir labels dos campos
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem'
        }

#Data como calendário
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulário de reserva

class ReservaForm(forms.ModelForm):
    #meta dados do formulario
    class Meta: 
        #definir modelo base
        model = Reserva

        #definir quais os campos do formulário
        fields = ['nome_pet', 'telefone', 'data_reserva','observacoes']

        #definir os widgets 
        widgets = {
            'nome_pet': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira o nome do seu pet aqui'
                }
            ), 
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu telefone aqui'
                }
            ), 
            'data_reserva': DateInput(),
            'observacoes': forms.TextInput(
                attrs={
                    'placeholder': 'Digite as observações aqui'
                }
            )
        }

        #definir labels dos campos
        labels = {
            'nome_pet': 'Nome:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data de Reserva do Banho:',
            'observacoes': 'Observações:'
        }