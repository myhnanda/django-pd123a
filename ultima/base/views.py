from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
#aythenticate pega as infomações e retorna


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
            formulario.save
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
            formulario.save()
            sucesso = True
    
    #contexto da view de reserva

    contexto = {
        'sucesso': sucesso,
        'formulario' : formulario
    }

    # renderizar a página

    return render(request, 'reserva.html', contexto)

#request.POST pega as informações do dicionário 

def login_usuario(request):
    #quando for GET só vai devolver o formulário de autenticação para ele;
    if request.method == 'GET':
        contexto = {
            'formulario': AuthenticationForm()
        }
        return render(request, 'login.html', contexto)
    else: 
        nome_usuario = request.POST['username']
        senha = request.POST['password']
        usuario = authenticate(request, username = nome_usuario, password= senha)
        if usuario is not None:
            login(request,usuario)
            return redirect('inicio')
        

#View de logout

def logout_usuario(request):
    logout(request)
    return redirect('inicio')

#View de cadastro usuario

def cadastro_usuario(request):
    sucesso = False

    if request.method == 'GET':
        formulario = UserCreationForm()
    
    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            sucesso = True
    
    contexto = {
        'formulario':formulario,
        'sucesso': sucesso
    }

    return render(request,'cadastro.html', contexto)
        
