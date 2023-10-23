from django import forms
from datetime import date 
#ou from .models 
from reserva.models import Reserva

#formulário para reserva

class ReservaForm(forms.ModelForm):
    def clean_data_reserva(self):
        # pega as datas de reserva e de hoje
        data_reserva = self.cleaned_data["data_reserva"]
        hoje = date.today()

        # se a data de reserva for anterior a hoje, gera um erro
        if data_reserva is not None and data_reserva < hoje:
            raise forms.ValidationError('Não é possível reservar o banho para a data no passado. Tente outra data')        
        

        #validação do turno
        turno = self.data['turno']
        numero_reservas = Reserva.objects.filter(turno = turno, data_reserva = data_reserva).count()

        if numero_reservas >=4:
            raise forms.ValidationError('Já existem mais de 4 reservas para essa data e período! Tente outra data e período!')



        return data_reserva
    
    class Meta:
        model = Reserva
        fields = ['nome','email','nome_pet', 'data_reserva', 'turno', 'porte','observacoes']
