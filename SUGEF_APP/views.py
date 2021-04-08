import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .models import *


# Create your views here.

hora = timezone.now().hour - 3

def login(request):
    if 'logado' in request.session:
        return redirect('sugef_app_index')
    setores = {
        'viveiro':'Visitante',
        'bovsystem':'Visitante',
        'ovinosystem':'Visitante',
    }
    request.session['setores'] = setores
    return render(request, 'SUGEF_APP/login.html', {})

def logout(request):
    if 'logado' in request.session:
        request.session.flush()
    return redirect('sugef_app_login')

def validacao(request):
    if not 'logado' in request.session:
        login = request.POST["username"]
        senha = request.POST["password"]
        usuario = Usuario.objects.get(matricula=login)
        if usuario:
            if senha == usuario.senha:
                request.session['logado'] = True
                request.session['usuario'] = usuario.matricula
                permissoes = Acessa.objects.filter(usuario=usuario.id)
                for permissao in permissoes:
                    request.session['setores'][permissao.setor.nome] = permissao.permissao
                    if permissao.permissao == 'Bolsista':
                        return redirect(f'{permissao.setor.nome}_index')
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
    if 'logado' in request.session:
        return render(request, 'SUGEF_APP/index.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'SUGEF_APP/erro.html', {'erro': erro})

def about_us(request):
    if 'usuario' in request.session:
        return render(request, 'SUGEF_APP/about_us.html', {'hora':hora})
    else:
        return render(request, 'SUGEF_APP/about_us.html', {'hora':hora})
