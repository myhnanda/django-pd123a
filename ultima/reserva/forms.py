from django import form

from datetime import date 
#ou from .models 
from reserva.models import Reserva

#formulário para reserva

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ['nome','email','nome_pet', 'data_reserva', 'turno', 'porte','observacoes']
        

