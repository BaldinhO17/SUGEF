from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validacao/', views.validacao, name='validacao'),
    path('erro/', views.erro, name='erro'),
    path('inicio/', views.index, name='index'),
    # Url animais
    path('animais/', views.animais, name='animais'),
    path('animais/carregar', views.carregar_animais, name='carregar_animais'),
    path('animais/cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('animais/<int:codigo>/mostrar/', views.mostrar_animal, name='mostrar_animal'),
    path('animais/<int:codigo>/apagar/', views.apagar_animal, name='apagar_animal'),
    path('animais/<int:codigo>/editar/', views.editar_animal, name='editar_animal'),
    # Url coberturas
    path('coberturas/', views.coberturas, name='coberturas'),
    path('coberturas/carregar', views.carregar_coberturas, name='carregar_coberturas'),
    path('coberturas/cadastrar/', views.cadastrar_cobertura, name='cadastrar_cobertura'),
    path('coberturas/<int:id>/apagar/', views.apagar_cobertura, name='apagar_cobertura'),
    path('coberturas/<int:id>/concluir/<str:termino>/<str:gestacao>/', views.concluir_cobertura, name='concluir_cobertura'),
    path('coberturas/<int:id>/editar/', views.editar_cobertura, name='editar_cobertura'),
    # Url registros financeiros
    path('registros-financeiros/', views.registros_financeiros, name='registros_financeiros'),
    path('registros-financeiros/carregar/', views.carregar_registros_financeiros, name='carregar_registros_financeiros'),
    path('registros-financeiros/cadastrar/', views.cadastrar_registro_financeiro, name='cadastrar_registro_financeiro'),
    path('registros-financeiros/<int:id>/apagar/', views.apagar_registro_financeiro, name='apagar_registro_financeiro'),
    path('registros-financeiros/<int:id>/editar/', views.editar_registro_financeiro, name='editar_registro_financeiro'),
    # Url gestacao
    path('gestacoes/', views.gestacoes, name='gestacoes'),
    path('gestacoes/carregar/', views.carregar_gestacoes, name='carregar_gestacoes'),
    path('gestacoes/cadastrar/', views.cadastrar_gestacao, name='cadastrar_gestacao'),
    path('gestacoes/<int:id>/apagar/', views.apagar_gestacao, name='apagar_gestacao'),
    path('gestacoes/<int:id>/concluir/<str:termino>/', views.concluir_gestacao, name='concluir_gestacao'),
    path('gestacoes/<int:id>/editar/', views.editar_gestacao, name='editar_gestacao'),
    # Url secacoes
    path('secacoes/', views.secacoes, name='secacoes'),
    path('secacoes/carregar/', views.carregar_secacoes, name='carregar_secacoes'),
    path('secacoes/cadastrar/', views.cadastrar_secacao, name='cadastrar_secacao'),
    path('secacoes/<int:id>/apagar/', views.apagar_secacao, name='apagar_secacao'),
    path('secacoes/<int:id>/editar/', views.editar_secacao, name='editar_secacao'),
    # Url estoque
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/carregar/', views.carregar_estoque, name='carregar_estoque'),
    path('estoque/cadastrar/', views.cadastrar_material, name='cadastrar_material'),
    path('estoque/<int:id>/apagar/', views.apagar_material, name='apagar_material'),
    path('estoque/<int:id>/editar/', views.editar_material, name='editar_material'),
    path('estoque/controle/', views.controle_estoque, name='controle_estoque'),
    path('estoque/controle/carregar/', views.carregar_controle_estoque, name='carregar_controle_estoque'),
    path('estoque/controle/cadastrar/saida/', views.cadastrar_saida_estoque, name='cadastrar_saida_estoque'),
    path('estoque/controle/cadastrar/entrada/', views.cadastrar_entrada_estoque, name='cadastrar_entrada_estoque'),
    path('estoque/controle/<int:id>/apagar/', views.apagar_controle_estoque, name='apagar_controle_estoque'),
    path('estoque/controle/<int:id>/editar/', views.editar_controle_estoque, name='editar_controle_estoque'),
    # Url producoes de leite
    path('producoes-de-leite/', views.producoes_de_leite, name='producoes_de_leite'),
    path('producoes-de-leite/graficos/', views.graficos_producoes_de_leite, name='graficos_producoes_de_leite'),
    path('producoes-de-leite/graficos/<int:femea>/<str:inicio>/<str:fim>/', views.carregar_graficos_producoes_de_leite, name='carregar_graficos_producoes_de_leite'),
    path('producoes-de-leite/carregar/', views.carregar_producoes_de_leite, name='carregar_producoes_de_leite'),
    path('producoes-de-leite/cadastrar/', views.cadastrar_producao_de_leite, name='cadastrar_producao_de_leite'),
    path('producoes-de-leite/<int:id>/apagar/', views.apagar_producao_de_leite, name='apagar_producao_de_leite'),
    path('producoes-de-leite/<int:id>/editar/', views.editar_producao_de_leite, name='editar_producao_de_leite'),
    # Url saidas de leite
    path('saidas-de-leite/', views.saidas_de_leite, name='saidas_de_leite'),
    path('saidas-de-leite/carregar/', views.carregar_saidas_de_leite, name='carregar_saidas_de_leite'),
    path('saidas-de-leite/cadastrar/', views.cadastrar_saida_de_leite, name='cadastrar_saida_de_leite'),
    path('saidas-de-leite/<int:id>/apagar/', views.apagar_saida_de_leite, name='apagar_saida_de_leite'),
    path('saidas-de-leite/<int:id>/editar/', views.editar_saida_de_leite, name='editar_saida_de_leite')

    
]
