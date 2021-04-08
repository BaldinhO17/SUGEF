from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login, name='sugef_app_login'),
    path('sugef_app/validacao/', views.validacao, name='sugef_app_validacao'),
    path('sugef_app/erro/', views.erro, name='sugef_app_erro'),
    path('sugef_app/inicio/', views.index, name='sugef_app_index'),
    path('sugef_app/<str:setor>/', views.redirecionar_setor, name='sugef_app_redirecionar_setor'),

    path('about_us/', views.about_us, name='about_us'),
]