from django import forms


# Formulario contato
class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)


# Formulário de reserva
class ReservaForm(forms.Form):
    nome_pet = forms.CharField()
    telefone = forms.CharField()
    data_reserva = forms.DateField()
    observacoes = forms.CharField(widget=forms.Textarea)