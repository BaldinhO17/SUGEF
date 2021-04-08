from django.urls import path
from . import views

urlpatterns = [
    path('bovsystem/', views.login, name='bovsystem_login'),
    path('bovsystem/acessar/<str:permissao>/<str:usuario>', views.acessar, name='bovsystem_acessar'),
    path('bovsystem/validacao/', views.validacao, name='bovsystem_validacao'),
    path('bovsystem/erro/', views.erro, name='bovsystem_erro'),
    path('bovsystem/inicio/', views.index, name='bovsystem_index'),
    # Url animais
    path('bovsystem/animais/', views.animais, name='bovsystem_animais'),
    path('bovsystem/animais/carregar', views.carregar_animais, name='bovsystem_carregar_animais'),
    path('bovsystem/animais/cadastrar/', views.cadastrar_animal, name='bovsystem_cadastrar_animal'),
    path('bovsystem/animais/<int:codigo>/mostrar/', views.mostrar_animal, name='bovsystem_mostrar_animal'),
    path('bovsystem/animais/<int:codigo>/apagar/', views.apagar_animal, name='bovsystem_apagar_animal'),
    path('bovsystem/animais/<int:codigo>/editar/', views.editar_animal, name='bovsystem_editar_animal'),
    # Url coberturas
    path('bovsystem/coberturas/', views.coberturas, name='bovsystem_coberturas'),
    path('bovsystem/coberturas/carregar', views.carregar_coberturas, name='bovsystem_carregar_coberturas'),
    path('bovsystem/coberturas/cadastrar/', views.cadastrar_cobertura, name='bovsystem_cadastrar_cobertura'),
    path('bovsystem/coberturas/<int:id>/apagar/', views.apagar_cobertura, name='bovsystem_apagar_cobertura'),
    path('bovsystem/coberturas/<int:id>/concluir/<str:termino>/<str:gestacao>/', views.concluir_cobertura, name='bovsystem_concluir_cobertura'),
    path('bovsystem/coberturas/<int:id>/editar/', views.editar_cobertura, name='bovsystem_editar_cobertura'),
    # Url registros financeiros
    path('bovsystem/registros-financeiros/', views.registros_financeiros, name='bovsystem_registros_financeiros'),
    path('bovsystem/registros-financeiros/carregar/', views.carregar_registros_financeiros, name='bovsystem_carregar_registros_financeiros'),
    path('bovsystem/registros-financeiros/cadastrar/', views.cadastrar_registro_financeiro, name='bovsystem_cadastrar_registro_financeiro'),
    path('bovsystem/registros-financeiros/<int:id>/apagar/', views.apagar_registro_financeiro, name='bovsystem_apagar_registro_financeiro'),
    path('bovsystem/registros-financeiros/<int:id>/editar/', views.editar_registro_financeiro, name='bovsystem_editar_registro_financeiro'),
    # Url gestacao
    path('bovsystem/gestacoes/', views.gestacoes, name='bovsystem_gestacoes'),
    path('bovsystem/gestacoes/carregar/', views.carregar_gestacoes, name='bovsystem_carregar_gestacoes'),
    path('bovsystem/gestacoes/cadastrar/', views.cadastrar_gestacao, name='bovsystem_cadastrar_gestacao'),
    path('bovsystem/gestacoes/<int:id>/apagar/', views.apagar_gestacao, name='bovsystem_apagar_gestacao'),
    path('bovsystem/gestacoes/<int:id>/concluir/<str:termino>/', views.concluir_gestacao, name='bovsystem_concluir_gestacao'),
    path('bovsystem/gestacoes/<int:id>/editar/', views.editar_gestacao, name='bovsystem_editar_gestacao'),
    # Url secacoes
    path('bovsystem/secacoes/', views.secacoes, name='bovsystem_secacoes'),
    path('bovsystem/secacoes/carregar/', views.carregar_secacoes, name='bovsystem_carregar_secacoes'),
    path('bovsystem/secacoes/cadastrar/', views.cadastrar_secacao, name='bovsystem_cadastrar_secacao'),
    path('bovsystem/secacoes/<int:id>/apagar/', views.apagar_secacao, name='bovsystem_apagar_secacao'),
    path('bovsystem/secacoes/<int:id>/editar/', views.editar_secacao, name='bovsystem_editar_secacao'),
    # Url estoque
    path('bovsystem/estoque/', views.estoque, name='bovsystem_estoque'),
    path('bovsystem/estoque/carregar/', views.carregar_estoque, name='bovsystem_carregar_estoque'),
    path('bovsystem/estoque/cadastrar/', views.cadastrar_material, name='bovsystem_cadastrar_material'),
    path('bovsystem/estoque/<int:id>/apagar/', views.apagar_material, name='bovsystem_apagar_material'),
    path('bovsystem/estoque/<int:id>/editar/', views.editar_material, name='bovsystem_editar_material'),
    path('bovsystem/estoque/controle/', views.controle_estoque, name='bovsystem_controle_estoque'),
    path('bovsystem/estoque/controle/carregar/', views.carregar_controle_estoque, name='bovsystem_carregar_controle_estoque'),
    path('bovsystem/estoque/controle/cadastrar/saida/', views.cadastrar_saida_estoque, name='bovsystem_cadastrar_saida_estoque'),
    path('bovsystem/estoque/controle/cadastrar/entrada/', views.cadastrar_entrada_estoque, name='bovsystem_cadastrar_entrada_estoque'),
    path('bovsystem/estoque/controle/<int:id>/apagar/', views.apagar_controle_estoque, name='bovsystem_apagar_controle_estoque'),
    path('bovsystem/estoque/controle/<int:id>/editar/', views.editar_controle_estoque, name='bovsystem_editar_controle_estoque'),
    # Url producoes de leite
    path('bovsystem/producoes-de-leite/', views.producoes_de_leite, name='bovsystem_producoes_de_leite'),
    path('bovsystem/producoes-de-leite/graficos/', views.graficos_producoes_de_leite, name='bovsystem_graficos_producoes_de_leite'),
    path('bovsystem/producoes-de-leite/graficos/<int:femea>/<str:inicio>/<str:fim>/', views.carregar_graficos_producoes_de_leite, name='bovsystem_carregar_graficos_producoes_de_leite'),
    path('bovsystem/producoes-de-leite/carregar/', views.carregar_producoes_de_leite, name='bovsystem_carregar_producoes_de_leite'),
    path('bovsystem/producoes-de-leite/cadastrar/', views.cadastrar_producao_de_leite, name='bovsystem_cadastrar_producao_de_leite'),
    path('bovsystem/producoes-de-leite/<int:id>/apagar/', views.apagar_producao_de_leite, name='bovsystem_apagar_producao_de_leite'),
    path('bovsystem/producoes-de-leite/<int:id>/editar/', views.editar_producao_de_leite, name='bovsystem_editar_producao_de_leite'),
    # Url saidas de leite
    path('bovsystem/saidas-de-leite/', views.saidas_de_leite, name='bovsystem_saidas_de_leite'),
    path('bovsystem/saidas-de-leite/carregar/', views.carregar_saidas_de_leite, name='bovsystem_carregar_saidas_de_leite'),
    path('bovsystem/saidas-de-leite/cadastrar/', views.cadastrar_saida_de_leite, name='bovsystem_cadastrar_saida_de_leite'),
    path('bovsystem/saidas-de-leite/<int:id>/apagar/', views.apagar_saida_de_leite, name='bovsystem_apagar_saida_de_leite'),
    path('bovsystem/saidas-de-leite/<int:id>/editar/', views.editar_saida_de_leite, name='bovsystem_editar_saida_de_leite')

    
]
