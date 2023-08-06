from django.shortcuts import render
from base.forms import ContatoForm


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
        'telefone': '(00) 99999-9999',
        'responsavel': 'Fulano de Tal'
    }

    return render(request, 'contato.html', contexto)