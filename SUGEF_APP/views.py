import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *


# Create your views here.

hora = timezone.now().hour - 3
usuario = None
logado = False
setores = {
    'viveiro':'Visitante',
    'bovsystem':'Visitante',
    'ovinosystem':'Visitante',
}

def login(request):
    global logado
    logado = False
    return render(request, 'SUGEF_APP/login.html', {})

def validacao(request):
    global logado, usuario, setores
    if not logado:
        login = request.POST["username"]
        senha = request.POST["password"]
        user = Usuario.objects.get(matricula=login)
        if user:
            if senha == user.senha:
                logado = True
                usuario = user
                permissoes = Acessa.objects.filter(usuario=user.id)
                for permissao in permissoes:
                    setores[permissao.setor.nome] = permissao.permissao
                    if permissao.permissao == 'Bolsista':
                        return redirect(f'{permissao.setor.nome}_acessar', permissao='Bolsista', usuario=usuario.nome)
                return redirect('sugef_app_index')
            else:
                return render(request, 'SUGEF_APP/login.html', {'mensagem':"Usuário ou senha incorretos"})
        else:
            return render(request, 'SUGEF_APP/login.html', {'mensagem':"Usuário não existe"})
    else:
        return redirect('sugef_app_login')

def erro(request):
    erro = 'É preciso o login para acessar esta página'
    return render(request, 'SUGEF_APP/erro.html', {'erro': erro})

def index(request):
    global logado
    if logado:
        return render(request, 'SUGEF_APP/index.html', {'hora':hora, 'nome':usuario.nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'SUGEF_APP/erro.html', {'erro': erro})

def redirecionar_setor(request, setor):
    global logado, setores
    if logado:
        return redirect(f'{setor}_acessar', permissao=setores[setor], usuario=usuario.nome)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'SUGEF_APP/erro.html', {'erro': erro})

def about_us(request):
    global usuario
    if usuario:
        return render(request, 'SUGEF_APP/about_us.html', {'hora':hora, 'nome':usuario.nome})
    else:
        return render(request, 'SUGEF_APP/about_us.html', {'hora':hora})
