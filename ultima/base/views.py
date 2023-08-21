from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    #Definir sucesso, para indicar se o envio da mensagem foi correto ou não7
    sucesso = False

    if request.method == 'GET':
        formulario = ContatoForm()

    #Se for o metodo POST
    else:
        formulario = ContatoForm(request.POST)
        if formulario.is_valid():
            sucesso = True

    #Definir o contexto da view contato

    contexto = {
        'sucesso': sucesso,
        'formulario': formulario,
        'fone': '(99) 99999-9999',
        'responsavel': 'Fulano de Tal'
    }

    return render(request, 'contato.html', contexto)

#View reserva de banho do pet

def reserva(request):
    #sucesso no envio da mensagem
    sucesso = False

    #método da requisição é GET
    if request.method == "GET":
        formulario = ReservaForm()

    #método POST

    else: 
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            sucesso = True
    
    #contexto da view de reserva

    contexto = {
        'sucesso': sucesso,
        'formulario' : formulario
    }

    # renderizar a página

    return render(request, 'reserva.html', contexto)