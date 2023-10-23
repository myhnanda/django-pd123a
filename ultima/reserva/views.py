from django.shortcuts import render

# Create your views here.
from reserva.forms import ReservaForm

#definir view de reserva

def criar_reserva(request):
    #definir variável sucesso
    sucesso = False

    #$MÉTODO GET
    # code Isa
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_reserva.html', contexto)

    """if request.method =='GET':
        formulario =ReservaForm()
    
    #MÉTODO POST

    else:
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            sucesso = True"""
        
    
    contexto = {
        'sucesso': sucesso,
        'formulario': formulario
    }

    return render(request, 'criar_reserva.html', contexto)