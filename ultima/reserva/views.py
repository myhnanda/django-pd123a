from django.shortcuts import render

# Create your views here.
from reserva.forms import ReservaForm

#definir view de reserva

def criar_reserva(request):
    #definir variável sucesso
    sucesso = False

    #$MÉTODO GET

    if request.method =='GET':
        formulario =ReservaForm()
    
    #MÉTODO POST

    else:
        formulário = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            sucesso = True
        
    
    contexto = {
        'sucesso': sucesso,
        'formulario': formulario
    }

    return render(request, 'criar_reserva.html', contexto)