from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from .models import *

hora = timezone.now().hour - 3
logado = False

def acessar(request, permissao, usuario):
    global  logado
    logado = True
    return redirect('viveiro_index')


def index(request):
    global logado
    if logado:
        return render(request, 'Viveiro/index.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def alunos(request):
    global logado
    if logado:
        return render(request, 'Viveiro/alunos.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def plantas(request):
    global logado
    if logado:
        return render(request, 'Viveiro/plantas.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_carregar_plantas(request):
    global logado
    if logado:
        plantas = Plantas.objects.all()
        dados = []
        for planta in plantas:
            dados.append(
                [
                    planta.especie,
                    planta.tipo,
                    planta.producao,
                    planta.doacao,
                    planta.venda,
                    planta.extravio,
                    planta.ifrn,
                    
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_adicionar_plantas(request):
    global logado
    if logado:
        especie = request.POST['especie']
        tipo = request.POST['tipo']
        producao = request.POST['producao']
        doacao = request.POST['doacao']
        venda = request.POST['venda']
        extravio = request.POST['extravio']
        ifrn = request.POST['ifrn']
        
        planta = Plantas(especie=especie, tipo=tipo, producao=producao, doacao=doacao, venda=venda, extravio=extravio, ifrn=ifrn)
        planta.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_editar_plantas(request):
    global logado
    if logado:
        especie = request.POST['especie']
        planta = Plantas.objects.get(especie=especie)
        planta.especie = request.POST['especie']
        planta.tipo = request.POST['tipo']
        planta.producao = request.POST['producao']
        planta.doacao = request.POST['doacao']
        planta.venda = request.POST['venda']
        planta.extravio = request.POST['extravio']
        planta.ifrn = request.POST['ifrn']
        
        planta.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_apagar_plantas(request):
    global logado
    if logado:
        especie = request.POST['especie']
        planta = Plantas.objects.get(especie=especie)
        planta.delete()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_carregar_visitas(request):
    global logado
    if logado:
        visitas = Visitas.objects.all()
        dados = []
        for visita in visitas:
            dados.append(
                [
                    visita.cod,
                    visita.data,
                    visita.hora,
                    visita.visitante,
                    
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_adicionar_visitas(request):
    global logado
    if logado:
        cod = request.POST['cod']
        data = request.POST['data']
        hora = request.POST['hora']
        visitante = request.POST['visitante']
        
        visita = Visitas(cod=cod, data=data, hora=hora, visitante=visitante)
        visita.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_editar_visitas(request):
    global logado
    if logado:
        cod = request.POST['cod']
        visita = Visitas.objects.get(cod=cod)
        
        visita.data = request.POST['data']
        visita.hora = request.POST['hora']
        visita.visitante = request.POST['visitante']
        
        visita.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_apagar_visitas(request):
    global logado
    if logado:
        cod = request.POST['cod']
        visita = Visitas.objects.get(cod=cod)
        visita.delete()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_carregar_insumos(request):
    global logado
    if logado:
        insumos = Insumos.objects.all()
        dados = []
        for insumo in insumos:
            dados.append(
                [
                    insumo.cod,
                    insumo.tipo,
                    insumo.marca,
                    insumo.desc,
                    insumo.quant,
                    
                ]
            )
        resposta = {"data":dados}
        return JsonResponse(resposta)
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_adicionar_insumos(request):
    global logado
    if logado:
        cod = request.POST['cod']
        tipo = request.POST['tipo']
        marca = request.POST['marca']
        desc = request.POST['desc']
        quant = request.POST['quant']
        
        insumo = Insumos(cod=cod, tipo=tipo, marca=marca, desc=desc, quant=quant)
        insumo.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_editar_insumos(request):
    global logado
    if logado:
        cod = request.POST['cod']
        insumo = Insumos.objects.get(cod=cod)
        
        insumo.tipo = request.POST['tipo']
        insumo.marca = request.POST['marca']
        insumo.desc = request.POST['desc']
        insumo.quant = request.POST['quant']
        insumo.save()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def se_apagar_insumos(request):
    global logado
    if logado:
        cod = request.POST['cod']
        insumo = Insumos.objects.get(cod=cod)
        insumo.delete()
        return HttpResponse('')
    else:
        return HttpResponseNotFound('É preciso login.')
        

def objetos(request):
    global logado
    if logado:
        return render(request, 'Viveiro/objetos.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def turmas(request):
    global logado
    if logado:
        return render(request, 'Viveiro/turmas.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def plantas(request):
    global logado
    if logado:
        return render(request, 'Viveiro/plantas.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def visitas(request):
    global logado
    if logado:
        return render(request, 'Viveiro/visitas.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        

def insumos(request):
    global logado
    if logado:
        return render(request, 'Viveiro/insumos.html', {'hora':hora})
    else:
        return HttpResponseNotFound('É preciso login.')
        
