import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Avg, Count, Min, Sum
from .models import *
from .forms import *


# Create your views here.

hora = timezone.now().hour - 3
nome = ''
logado = False
setor = "Bovinocultura"
permissao_setor = "Visitante"

def setLogado(request):
    global logado
    logado = not logado

def login(request):
    global logado
    logado = False
    return render(request, 'BovSystem/login.html', {})

def validacao(request):
    global logado, nome, setor, permissao_setor
    if not logado:
        login = request.POST["username"]
        senha = request.POST["pass"]
        usuarios = Usuario.objects.all()
        for user in usuarios:
            if login == user.matricula and senha == user.senha:
                setLogado(request)
                nome = user.nome
                permissao = Acessa.objects.filter(usuario=user.id, setor='Bovinocultura')[0].permissao
                return redirect('bovsystem_index')
        else:
            return render(request, 'BovSystem/login.html', {'mensagem':"Usuário ou senha incorretos"})
    else:
        return redirect('bovsystem_login')


def acessar(request, permissao, usuario):
    global  logado, nome, permissao_setor
    logado = True
    nome = usuario
    permissao_setor = permissao
    return redirect('bovsystem_index')



def erro(request):
    erro = 'É preciso o login para acessar esta página'
    return render(request, 'BovSystem/erro.html', {'erro': erro})

def index(request):
    global logado
    if logado:
        return render(request, 'BovSystem/index.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def animais(request):
    global logado
    if logado:
        return render(request, 'BovSystem/animais.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def coberturas(request):
    global logado
    if logado:
        return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def registros_financeiros(request):
    global logado
    if logado:
        return render(request, 'BovSystem/registros_financeiros.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def secacoes(request):
    global logado
    if logado:
        return render(request, 'BovSystem/secacoes.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def estoque(request):
    global logado
    if logado:
        return render(request, 'BovSystem/estoque.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def controle_estoque(request):
    global logado
    if logado:
        return render(request, 'BovSystem/estoque/controle_estoque.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def gestacoes(request):
    global logado
    if logado:
        return render(request, 'BovSystem/gestacoes.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def producoes_de_leite(request):
    global logado
    if logado:
        return render(request, 'BovSystem/producoes_de_leite.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def saidas_de_leite(request):
    global logado
    if logado:
        return render(request, 'BovSystem/saidas_de_leite.html', {'hora':hora, 'nome':nome})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página Animal ------

def carregar_animais(request):
    global logado
    if logado:
        animais = Animal.objects.all()
        dados = []
        for animal in animais:
            dados.append(
                [
                    animal.codigo,
                    animal.nome,
                    animal.sexo,
                    animal.peso,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_animal(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            machos=Animal.objects.filter(sexo="Masculino")
            femeas=Animal.objects.filter(sexo="Feminino")
            animal_form = AnimalForm(dict(list(request.POST.items())[1:6]) or None)
            print(list(request.POST.items())[1:6])
            nascimento_form = NascimentoForm(dict(list(request.POST.items())[6:]) or None)
            print(list(request.POST.items())[6:])
            if animal_form.is_valid():
                animal_form.save()

                if nascimento_form.is_valid() and (request.POST['tipo-cadastro']=='nascimento'):
                    nascimento_form.save()

                if ((request.POST['tipo-cadastro']!='nascimento') or (nascimento_form.is_valid())):
                    return redirect('bovsystem_animais')
            data={
                'machos':machos,
                'femeas':femeas,
                'animal_form':animal_form,
                'nascimento_form':nascimento_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/animais/cadastrar_animal.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/animais.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_animal(request, codigo):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            animal = Animal.objects.get(codigo=codigo)
            form = AnimalForm(request.POST or None, instance=animal)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_animais')

            return render(request, 'BovSystem/animais/editar_animal.html', {'form':form,'animal': animal, 'hora':hora, 'nome':nome})
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/animais.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_animal(request, codigo):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            animal = Animal.objects.get(codigo=codigo)
            animal.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def mostrar_animal(request, codigo):
    global logado
    if logado:
        animal = Animal.objects.get(codigo=codigo)
        nascimento = ''
        try:
            nascimento = Nascimento.objects.get(filhote=codigo)
        except:
            print("Sem registro")
        filhos = []
        coberturas = []
        gravidezes = []
        secacoes = []
        if animal.sexo == 'Masculino':
            try:
                for nascimento_filho in Nascimento.objects.filter(pai=codigo):
                    filhos.append(nascimento_filho.filhote)
            except:
                print("Sem registro")
            try:
                for cobertura in Cobertura.objects.filter(macho=codigo):
                    coberturas.append(cobertura)
            except:
                print("Sem registro")
        else:
            try:
                for nascimento_filho in Nascimento.objects.filter(matriz=codigo):
                    filhos.append(nascimento_filho.filhote)
            except:
                print("Sem registro")
            try:
                for cobertura in Cobertura.objects.filter(femea=codigo):
                    coberturas.append(cobertura)
            except:
                print("Sem registro")
            try:
                for gravidez in Gravidez.objects.filter(animal=codigo):
                    gravidezes.append(gravidez)
            except:
                print("Sem registro")
            try:
                for secacao in Secacao.objects.filter(matriz=codigo):
                    secacoes.append(secacao)
            except:
                print("Sem registro")
        data = {
            'animal': animal,
            'nascimento': nascimento,
            'filhos': filhos,
            'coberturas': coberturas,
            'gravidezes' : gravidezes,
            'secacoes': secacoes,
            'hora':hora,
            'nome':nome
        }

        return render(request, 'BovSystem/animais/mostrar_animal.html', data)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_nascimento(request, data_nasc=False):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            animal_form = AnimalForm(request.POST or None)
            if animal_form.is_valid():
                animal_form.save()
                gestacoes = Gravidez.objects.filter(ativa=False)
                for gestacao in gestacoes:
                    if not gestacao.termino:
                        gestacao.termino = request.POST['data']
                        nascimento = Nascimento(data= request.POST['data'], pai = gestacao.cobertura.macho, matriz = gestacao.animal, filhote = Animal.objects.get(codigo=request.POST['codigo']), peso_nasc = request.POST['peso'])
                        gestacao.save()
                        nascimento.save()

                return render(request, 'BovSystem/animais.html', {'hora':hora, 'nome':nome})
            data={
                'data_nasc':data_nasc,
                'animal_form':animal_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/nascimentos/cadastrar_nascimento.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página cobertura ------

def carregar_coberturas(request):
    global logado
    if logado:
        coberturas = Cobertura.objects.all()
        dados = []
        for cobertura in coberturas:
            termino = 'Em andamento' if cobertura.ativa else cobertura.termino
            dados.append(
                [
                    cobertura.id,
                    cobertura.inicio,
                    cobertura.femea.nome,
                    cobertura.macho.nome,
                    termino,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_cobertura(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            machos=Animal.objects.filter(sexo="Masculino")
            femeas=Animal.objects.filter(sexo="Feminino")
            cobertura_form = CoberturaForm(request.POST or None)
            if cobertura_form.is_valid():
                cobertura_form.save()
                return redirect('bovsystem_coberturas')
            data={
                'machos':machos,
                'femeas':femeas,
                'cobertura_form':cobertura_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/coberturas/cadastrar_cobertura.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_cobertura(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            machos=Animal.objects.filter(sexo="Masculino")
            femeas=Animal.objects.filter(sexo="Feminino")
            cobertura = Cobertura.objects.get(id=id)
            form = CoberturaForm(request.POST or None, instance=cobertura)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_coberturas')

            data={
                'machos':machos,
                'femeas':femeas,
                'form':form,
                'cobertura': cobertura,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/coberturas/editar_cobertura.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_cobertura(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            cobertura = Cobertura.objects.get(id=id)
            cobertura.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def concluir_cobertura(request, id, termino, gestacao):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            cobertura = Cobertura.objects.get(id=id)
            cobertura.ativa = False
            cobertura.termino = termino
            if gestacao=='true':
                gestacoes = Gravidez.objects.filter(animal=cobertura.femea.codigo)
                for gestacao_anterior in gestacoes:
                    if gestacao_anterior.ativa:
                        mensagem = ""+cobertura.femea.nome+" já tem gestação em andamento!"
                        return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
                gestacao = Gravidez(inicio=cobertura.termino, animal=cobertura.femea, cobertura=cobertura, ativa=True)
                gestacao.save()
            cobertura.save()
            return redirect('bovsystem_coberturas')
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/coberturas.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página Registros Financeiro ------

def carregar_registros_financeiros(request):
    global logado
    if logado:
        registros_financeiros = Registro_Financeiro.objects.all()
        dados = []
        for registro_financeiro in registros_financeiros:
            dados.append(
                [
                    registro_financeiro.id,
                    registro_financeiro.descricao,
                    registro_financeiro.valor,
                    registro_financeiro.data,
                    registro_financeiro.hora,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_registro_financeiro(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            registro_financeiro_form = Registro_FinanceiroForm(request.POST or None)
            if registro_financeiro_form.is_valid():
                registro_financeiro_form.save()
                return redirect('bovsystem_registros_financeiros')
            data={
                'registro_financeiro_form':registro_financeiro_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/registros_financeiros/cadastrar_registro_financeiro.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/registros_financeiros.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_registro_financeiro(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            registro_financeiro = Registro_Financeiro.objects.get(id=id)
            form = Registro_FinanceiroForm(request.POST or None, instance=registro_financeiro)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_registros_financeiros')

            data={
                'form':form,
                'registro_financeiro': registro_financeiro,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/registros_financeiros/editar_registro_financeiro.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/registros_financeiros.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_registro_financeiro(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            registro_financeiro = Registro_Financeiro.objects.get(id=id)
            registro_financeiro.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})


# ------ Funções da página Estoque ------

def carregar_estoque(request):
    global logado
    if logado:
        estoque = Material.objects.all()
        dados = []
        for material in estoque:
            dados.append(
                [
                    material.id,
                    material.nome,
                    material.tipo,
                    material.validade,
                    material.quantidade,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_material(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            material_form = MaterialForm(request.POST or None)
            if material_form.is_valid():
                material_form.save()
                return redirect('bovsystem_estoque')
            data={
                'material_form':material_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/estoque/cadastrar_material.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/estoque.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_material(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            material = Material.objects.get(id=id)
            form = MaterialForm(request.POST or None, instance=material)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_estoque')

            data={
                'form':form,
                'material': material,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/estoque/editar_material.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/estoque.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_material(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            material = Material.objects.get(id=id)
            material.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções do Controle Estoque ----

def carregar_controle_estoque(request):
    global logado
    if logado:
        entradas_saidas = Entrada_Saida_Estoque.objects.all()
        dados = []
        for entrada_saida in entradas_saidas:
            dados.append(
                [
                    entrada_saida.id,
                    entrada_saida.tipo,
                    entrada_saida.material.nome,
                    entrada_saida.data,
                    entrada_saida.hora,
                    entrada_saida.descricao,
                    ''
                ]
            )
        for dado in dados:
            print(dado)
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_entrada_estoque(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            materiais = Material.objects.all()
            if ("valor" in request.POST) and ("data" in request.POST) and ("hora" in request.POST):
                material = Material.objects.get(id=request.POST["material"])
                descricao = request.POST["quantidade"] + " - " + material.nome
                gasto = Registro_Financeiro(descricao=descricao, valor=-float(request.POST["valor"]), data=request.POST["data"], hora=request.POST["hora"])
                gasto.save()
            controle_estoque_form = Entrada_Saida_EstoqueForm(request.POST or None)
            if controle_estoque_form.is_valid():
                controle_estoque_form.gasto = gasto.id
                controle_estoque_form.save()
                material.quantidade+=int(request.POST["quantidade"])
                material.save()
                return redirect('bovsystem_controle_estoque')
            data={
                'materiais':materiais,
                'tipo':"Entrada",
                'controle_estoque_form':controle_estoque_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/estoque/controle_estoque/cadastrar_controle_estoque.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/estoque/controle_estoque.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_saida_estoque(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            materiais = Material.objects.all()
            controle_estoque_form = Entrada_Saida_EstoqueForm(request.POST or None)
            if controle_estoque_form.is_valid():
                controle_estoque_form.save()
                return redirect('bovsystem_controle_estoque')
            data={
                'materiais':materiais,
                'tipo':"Saida",
                'controle_estoque_form':controle_estoque_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/estoque/controle_estoque/cadastrar_controle_estoque.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/estoque/controle_estoque.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_controle_estoque(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            materiais = Material.objects.all()
            controle_estoque = Entrada_Saida_Estoque.objects.get(id=id)
            form = Entrada_Saida_EstoqueForm(request.POST or None, instance=controle_estoque)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_controle_estoque')

            data={
                'materiais':materiais,
                'form':form,
                'controle_estoque': controle_estoque,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/estoque/controle_estoque/editar_controle_estoque.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/estoque/controle_estoque.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_controle_estoque(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            controle_estoque = Entrada_Saida_Estoque.objects.get(id=id)
            controle_estoque.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página Gestação ------

def carregar_gestacoes(request):
    global logado
    if logado:
        termino = ''
        ativa= ''
        gestacoes = Gravidez.objects.all()
        dados = []
        for gestacao in gestacoes:
            if gestacao.ativa:
                gestacoes_anteriores = Gravidez.objects.filter(animal=gestacao.animal, ativa=False)
                tempo_medio_gestacoes = 283
                quant_gestacoes_anteriores = 0
                duracao_gestacoes_anteriores = 0
                for gestacao_anterior in gestacoes_anteriores:
                    quant_gestacoes_anteriores+=1
                    inicio = str(gestacao_anterior.inicio).split('-')
                    dia_inicio = int(inicio[2])
                    mes_inicio = int(inicio[1])
                    ano_inicio = int(inicio[0])
                    inicio = dia_inicio + (mes_inicio*30) + (ano_inicio*365)
                    termino = str(gestacao_anterior.termino).split('-')
                    dia_termino = int(termino[2])
                    mes_termino = int(termino[1])
                    ano_termino = int(termino[0])
                    termino = dia_termino + (mes_termino*30) + (ano_termino*365)
                    duracao_gestacoes_anteriores += termino - inicio
                if not quant_gestacoes_anteriores == 0:
                    tempo_medio_gestacoes = int(duracao_gestacoes_anteriores/quant_gestacoes_anteriores)
                inicio = str(gestacao.inicio).split('-')
                dia_previsao = tempo_medio_gestacoes+(int(inicio[2]))
                mes_previsao = int(inicio[1])
                ano_previsao = int(inicio[0])
                if dia_previsao > 30:
                    if dia_previsao%30==0:
                        mes_previsao += (int(dia_previsao/30)-1)
                        dia_previsao= 30
                    else:
                        mes_previsao += int(dia_previsao/30)
                        dia_previsao -= (int(dia_previsao/30) * 30)
                    if mes_previsao>12:
                        ano_previsao += 1
                        mes_previsao -= 12
                if mes_previsao == 2 and dia_previsao > 28:
                    mes_previsao+=1
                    dia_previsao-=28
                if dia_previsao < 10:
                    dia_previsao = '0' + str(dia_previsao)
                if mes_previsao < 10:
                    mes_previsao = '0' + str(mes_previsao)
                termino = '{}-{}-{}'.format(ano_previsao, mes_previsao, dia_previsao)
                ativa = 'Em andamento'
            else:
                termino = gestacao.termino
                ativa = 'Finalizada'
            dados.append(
                [
                    gestacao.id,
                    gestacao.animal.nome,
                    gestacao.inicio,
                    ativa,
                    termino,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_gestacao(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            coberturas=Cobertura.objects.filter(ativa=True)
            gestacao_form = GravidezForm(request.POST or None)
            if gestacao_form.is_valid():
                gestacoes = Gravidez.objects.filter(animal=request.POST['animal'])
                for gestacao_anterior in gestacoes:
                    if gestacao_anterior.ativa:
                        mensagem = ""+gestacao_anterior.animal.nome+" já tem gestação em andamento!"
                        data={
                            'mensagem':mensagem,
                            'coberturas':coberturas,
                            'gestacao_form':gestacao_form,
                            'hora':hora,
                            'nome':nome
                        }
                        return render(request, 'BovSystem/gestacoes/cadastrar_gestacao.html', data)
                cobertura = Cobertura.objects.get(id=request.POST['cobertura'])
                cobertura.ativa = False
                cobertura.termino = request.POST['inicio']
                cobertura.save()
                gestacao_form.save()
                return redirect('bovsystem_gestacoes')
            data={
                'coberturas':coberturas,
                'gestacao_form':gestacao_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/gestacoes/cadastrar_gestacao.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/gestacoes.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_gestacao(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            animais=Animal.objects.filter(sexo="Feminino")
            gestacao = Gravidez.objects.get(id=id)
            form = GravidezForm(request.POST or None, instance=gestacao)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_gestacoes')

            data={
                'animais':animais,
                'form':form,
                'gestacao': gestacao,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/gestacoes/editar_gestacao.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/gestacoes.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_gestacao(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            gestacao = Gravidez.objects.get(id=id)
            gestacao.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def concluir_gestacao(request, id, termino):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            gestacao = Gravidez.objects.get(id=id)
            gestacao.ativa = False
            gestacao.save()
            return HttpResponse(cadastrar_nascimento(request, termino))
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/gestacoes.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})


# ------ Funções da página Secações ------

def carregar_secacoes(request):
    global logado
    if logado:
        secacoes = Secacao.objects.all()
        dados = []
        for secacao in secacoes:
            termino = 'Em andamento' if secacao.ativa else secacao.termino
            dados.append(
                [
                    secacao.id,
                    secacao.matriz.nome,
                    secacao.inicio,
                    secacao.leite,
                    termino,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_secacao(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            matrizes=Animal.objects.filter(sexo="Feminino")
            secacao_form = SecacaoForm(request.POST or None)
            secacao_form.fields["leite"].label = "Presença de leite"
            print(secacao_form.fields)
            if secacao_form.is_valid():
                secacao_form.save()
                return redirect('bovsystem_secacoes')
            data={
                'matrizes':matrizes,
                'secacao_form':secacao_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/secacoes/cadastrar_secacao.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/secacoes.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_secacao(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            matrizes=Animal.objects.filter(sexo="Feminino")
            secacao = Secacao.objects.get(id=id)
            form = SecacaoForm(request.POST or None, instance=secacao)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_secacoes')

            data={
                'matrizes':matrizes,
                'form':form,
                'secacao': secacao,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/secacoes/editar_secacao.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/secacoes.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_secacao(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            secacao = Secacao.objects.get(id=id)
            secacao.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página Produção de Leite ------

def carregar_producoes_de_leite(request):
    global logado
    if logado:
        producoes_de_leite = Produc_leite.objects.all()
        dados = []
        for producao_de_leite in producoes_de_leite:
            dados.append(
                [
                    producao_de_leite.id,
                    producao_de_leite.femea.nome,
                    producao_de_leite.quantidade,
                    producao_de_leite.data,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_producao_de_leite(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            femeas=Animal.objects.filter(sexo="Feminino")
            producao_de_leite_form = Produc_leiteForm(request.POST or None)
            if producao_de_leite_form.is_valid():
                producao_de_leite_form.save()
                return redirect('bovsystem_producoes_de_leite')
            data={
                'femeas':femeas,
                'producao_de_leite_form':producao_de_leite_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/producoes_de_leite/cadastrar_producao_de_leite.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/producoes_de_leite.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_producao_de_leite(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            femeas=Animal.objects.filter(sexo="Feminino")
            producao_de_leite = Produc_leite.objects.get(id=id)
            form = Produc_leiteForm(request.POST or None, instance=producao_de_leite)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_producoes_de_leite')

            data={
                'femeas':femeas,
                'form':form,
                'producao_de_leite': producao_de_leite,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/producoes_de_leite/editar_producao_de_leite.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/producoes_de_leite.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_producao_de_leite(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            producao_de_leite = Produc_leite.objects.get(id=id)
            producao_de_leite.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def graficos_producoes_de_leite(request):
    global logado
    if logado:
        femeas=Animal.objects.filter(sexo="Feminino")
        return render(request, 'BovSystem/producoes_de_leite/graficos_producoes_de_leite.html', {'hora':hora, 'nome':nome, 'femeas':femeas})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def carregar_graficos_producoes_de_leite(request, femea, inicio, fim):
    global logado
    if logado:
        producoes_de_leite = []
        if femea == 0:
            producoes_de_leite = Produc_leite.objects.filter(data__range=(inicio, fim)).annotate(Sum('quantidade')).order_by('data')
        else:
            producoes_de_leite = Produc_leite.objects.filter(femea=femea, data__range=(inicio, fim)).annotate(Sum('quantidade')).order_by('data')
        dados = [[],[]]
        for producao_de_leite in producoes_de_leite:
            dados[0].append(producao_de_leite.quantidade__sum)
            dados[1].append(producao_de_leite.data)
        resposta = {"dados":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

# ------ Funções da página Saídas de Leite ------

def carregar_saidas_de_leite(request):
    global logado
    if logado:
        saidas_de_leite = Saida_Leite.objects.all()
        dados = []
        for saida_de_leite in saidas_de_leite:
            valor = saida_de_leite.ganho.valor if saida_de_leite.ganho else '0.00'
            dados.append(
                [
                    saida_de_leite.id,
                    saida_de_leite.destino,
                    saida_de_leite.quantidade,
                    saida_de_leite.data,
                    saida_de_leite.responsavel,
                    valor,
                    ''
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def cadastrar_saida_de_leite(request):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            saida_de_leite_form = Saida_LeiteForm(request.POST or None)
            if saida_de_leite_form.is_valid():
                saida_de_leite_form.save()
                return redirect('bovsystem_saidas_de_leite')
            data={
                'saida_de_leite_form':saida_de_leite_form,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/saidas_de_leite/cadastrar_saida_de_leite.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/saidas_de_leite.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def editar_saida_de_leite(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Bolsista' or permissao_setor == 'Administrador':
            animais=Animal.objects.filter(sexo="Feminino")
            saida_de_leite = Saida_Leite.objects.get(id=id)
            form = Saida_LeiteForm(request.POST or None, instance=saida_de_leite)

            if form.is_valid():
                form.save()
                return redirect('bovsystem_saidas_de_leite')

            data={
                'form':form,
                'saida_de_leite': saida_de_leite,
                'hora':hora,
                'nome':nome
                }
            return render(request, 'BovSystem/saidas_de_leite/editar_saida_de_leite.html', data)
        else:
            mensagem = "Usuario não tem permissão para isso."
            return render(request, 'BovSystem/saidas_de_leite.html', {'hora':hora, 'nome':nome, 'mensagem':mensagem})
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

def apagar_saida_de_leite(request, id):
    global logado, permissao_setor
    if logado:
        if permissao_setor == 'Administrador':
            saida_de_leite = Saida_Leite.objects.get(id=id)
            saida_de_leite.delete()
            return HttpResponse('')
        else:
            mensagem= {'mensagem':"Usuario não tem permissão para isso."}
            return JsonResponse(mensagem)
    else:
        erro = 'É preciso o login para acessar esta página'
        return render(request, 'BovSystem/erro.html', {'erro': erro})

