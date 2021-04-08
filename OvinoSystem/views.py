import datetime
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .models import *
from SUGEF_APP.models import Usuario, Acessa, Setor

hora = timezone.now().hour - 3

def login(request):
    if 'logado' in request.session:
        return redirect('ovinosystem_index')
    setores = {
        'viveiro':'Visitante',
        'bovsystem':'Visitante',
        'ovinosystem':'Visitante',
    }
    request.session['setores'] = setores
    return render(request, 'OvinoSystem/login.html', {})

def logout(request):
    if 'logado' in request.session:
        request.session.flush()
    return redirect('sugef_app_login')

def validacao(request):
    if not 'logado' in request.session:
        login = request.POST["username"]
        senha = request.POST["pass"]
        usuario = Usuario.objects.get(matricula=login)
        if usuario:
            if senha == usuario.senha:
                request.session['logado'] = True
                request.session['usuario'] = usuario.matricula
                permissoes = Acessa.objects.filter(usuario=usuario.id)
                for permissao in permissoes:
                    request.session['setores'][permissao.setor.nome] = permissao.permissao
                    if (permissao.setor.nome == 'ovinosystem') and (permissao.permissao == 'Bolsista' or permissao.permissao == 'Administrador'):
                        return redirect('ovinosystem_index')
                else:
                    return redirect('sugef_app_index')
        else:
            return redirect('ovinosystem_login')
    else:
        return redirect('ovinosystem_login')

def erro(request):
    erro = 'É preciso o login para acessar esta página'
    return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def index(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/index.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def animais(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/animais.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def estoque(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/estoque.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def doenca(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/doenca.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})      

def vinculardoenca(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/vinculardoenca.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})      

def saida(request):
    if 'logado' in request.session:
        return render(request, 'OvinoSystem/saida.html', {'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})  

def modelos(dados, mod, acao):
    if 'logado' in request.session:
        if acao:
            if mod == 'M':
                return Material(tipo=dados[0], nome=dados[1], validade=dados[2], quantidade=dados[3])
            elif mod == 'A':           
                return Animal(codigo=dados[0], nome=dados[1], sexo=dados[2], peso=dados[3], especie=dados[4], raca=dados[5], pelagem=dados[6], data_nascimento=dados[7], registro=dados[8])
            elif mod == 'D':
                return Doenca(codigo=dados[0], nome=dados[1], descricao=dados[2])
            elif mod == 'V':
                return VincularDoenca(id=dados[0], animal=Animal.objects.get(codigo=dados[1]), doenca=Doenca.objects.get(codigo=dados[2]), dataregistro=dados[3])
            elif mod == 'S':
                return SaidaAnimal(codigo=dados[0], motivo=dados[1], saida=dados[2])
        else:
            if mod == 'M':
                return Material.objects.get(nome=dados)
            elif mod == 'A':
                return Animal.objects.get(codigo=dados)
            elif mod == 'D':
                return Doenca.objects.get(codigo=dados)
            elif mod == 'V':
                return VincularDoenca.objects.get(id=dados)   
            elif mod == 'S':
                return SaidaAnimal.objects.get(codigo=dados)
            else:
                return ''
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def adicionar(request):
    if 'logado' in request.session:
        dados = []
        for i in request.POST:
            if not i == 'modelo' and not i == 'csrfmiddlewaretoken':
                dados.append(request.POST[i])
        aux = modelos(dados, request.POST['modelo'], True)
        aux.save()
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def apagar(request):
    if 'logado' in request.session:
        aux = modelos(request.POST['codigo'], request.POST['modelo'], False)
        aux.delete()
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

# ------ Funções da página Animal ------

def carregar_animais(request):
    if 'logado' in request.session:
        animais = Animal.objects.all()
        dados = []
        for animal in animais:
            dados.append(
                [
                    animal.codigo,
                    animal.nome,
                    animal.sexo,
                    animal.peso,
                    animal.especie,
                    animal.raca,
                    animal.pelagem,
                    animal.data_nascimento,
                    animal.registro,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def info_animais(request):
    if 'logado' in request.session:
        codigo = request.POST['codigo']
        request.session['info'] = codigo
        return HttpResponse('')
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def carregar_info_animal(request, codigo):
    if 'logado' in request.session:  
        animal = Animal.objects.get(codigo=request.session['info'])
        animal = Animal.get_object_or_404(Animal, pk='codigo')
        return render(request, 'OvinoSystem/info_animais.html', {'animal': animal})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

def carregar_graf_produc(request):
    if 'logado' in request.session:
        animal = Animal.objects.get(nome=request.session['info'])
        return render(request, 'OvinoSystem/graficos.html', {'animal': animal, 'hora':hora, 'nome':Usuario.objects.get(matricula=request.session['usuario']).nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

# ------ Funções da página Estoque ------

def carregar_estoque(request):
    if 'logado' in request.session:
        estoque = Material.objects.all()
        dados = []
        for material in estoque:
            dados.append(
                [
                    material.tipo,
                    material.nome,
                    material.validade,
                    material.quantidade,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})
  

# ------ Funções da página Doença ------

def carregar_doenca(request):
    if 'logado' in request.session:
        registro = Doenca.objects.all()
        dados = []
        for doenca in registro:
            dados.append(
                [
                    doenca.codigo,
                    doenca.nome,
                    doenca.descricao,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})


# ------ Funções da página Doença ------

def carregar_vincular_doenca(request):
    if 'logado' in request.session:
        registro = VincularDoenca.objects.all()
        dados = []
        for vinculardoenca in registro:
            dados.append(
                [
                    vinculardoenca.id,
                    vinculardoenca.animal.codigo,
                    vinculardoenca.doenca.codigo,
                    vinculardoenca.dataregistro,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})

#-----------------GERENCIAR SAIDA---------------------
def carregar_saida(request):
    if 'logado' in request.session:
        registro = SaidaAnimal.objects.all()
        dados = []
        for saida in registro:
            dados.append(
                [
                    saida.codigo,
                    saida.motivo,
                    saida.saida,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'OvinoSystem/erro.html', {'erro': erro})