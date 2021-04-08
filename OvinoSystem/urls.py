from django.urls import path
from . import views

urlpatterns = [
    path('ovinosystem/', views.login, name='ovinosystem_login'),
    path('ovinosystem/logout/', views.logout, name='ovinosystem_logout'),
    path('ovinosystem/validacao/', views.validacao, name='ovinosystem_validacao'),
    path('ovinosystem/erro/', views.erro, name='ovinosystem_erro'),
    path('ovinosystem/inicio/', views.index, name='ovinosystem_index'),
    path('ovinosystem/adicionar/', views.adicionar, name='ovinosystem_adicionar'),
    path('ovinosystem/apagar/', views.apagar, name='ovinosystem_apagar'),
    path('ovinosystem/animais/', views.animais, name='ovinosystem_animais'),
    path('ovinosystem/animais/carregar/', views.carregar_animais, name='ovinosystem_carregar_animais'),
    path('ovinosystem/estoque/', views.estoque, name='ovinosystem_estoque'),
    path('ovinosystem/estoque/carregar/', views.carregar_estoque, name='ovinosystem_carregar_estoque'),
    path('ovinosystem/doenca/', views.doenca, name='ovinosystem_doenca'),
    path('ovinosystem/doenca/carregar/', views.carregar_doenca, name='ovinosystem_carregar_doenca'),
    path('ovinosystem/vinculardoenca/', views.vinculardoenca, name='ovinosystem_vincular_doenca'),
    path('ovinosystem/vinculardoenca/carregar/', views.carregar_vincular_doenca, name='ovinosystem_carregar_vincular_doenca'),
    path('ovinosystem/saida/', views.saida, name='ovinosystem_saida'),
    path('ovinosystem/saida/carregar/', views.carregar_saida, name='ovinosystem_carregar_saida'),
]
