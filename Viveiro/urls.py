from django.urls import path
from . import views

urlpatterns = [

    path('viveiro/', views.index, name='viveiro_index'),

    path('viveiro/alunos/', views.alunos, name='viveiro_alunos'),

    
    
    
    path('viveiro/logout/', views.logout, name='viveiro_logout'),
    path('viveiro/plantas/', views.plantas, name='viveiro_plantas'),
    path('viveiro/plantas/carregar/', views.se_carregar_plantas, name='viveiro_se_carregar_plantas'),
    path('viveiro/plantas/adicionar/', views.se_adicionar_plantas, name='viveiro_se_adicionar_plantas'),
    path('viveiro/plantas/editar/', views.se_editar_plantas, name='viveiro_se_editar_plantas'),
    path('viveiro/plantas/apagar/', views.se_apagar_plantas, name='viveiro_se_apagar_plantas'),
    path('viveiro/objetos/', views.objetos, name='viveiro_objetos'),
    
    path('viveiro/visitas/', views.visitas, name='viveiro_visitas'),
    path('viveiro/visitas/carregar/', views.se_carregar_visitas, name='viveiro_se_carregar_visitas'),
    path('viveiro/visitas/adicionar/', views.se_adicionar_visitas, name='viveiro_se_adicionar_visitas'),
    path('viveiro/visitas/editar/', views.se_editar_visitas, name='viveiro_se_editar_visitas'),
    path('viveiro/visitas/apagar/', views.se_apagar_visitas, name='viveiro_se_apagar_visitas'),

    path('viveiro/insumos/', views.insumos, name='viveiro_insumos'),
    path('viveiro/insumos/carregar/', views.se_carregar_insumos, name='viveiro_se_carregar_insumos'),
    path('viveiro/insumos/adicionar/', views.se_adicionar_insumos, name='viveiro_se_adicionar_insumos'),
    path('viveiro/insumos/editar/', views.se_editar_insumos, name='viveiro_se_editar_insumos'),
    path('viveiro/insumos/apagar/', views.se_apagar_insumos, name='viveiro_se_apagar_insumos'),
    
    path('viveiro/turmas/', views.turmas, name='viveiro_turmas'),



]