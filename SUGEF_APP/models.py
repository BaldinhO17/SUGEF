from django.db import models

# Create your models here.

class Usuario(models.Model):
    matricula = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)
    nome = models.CharField(max_length=64)

class Setor(models.Model):
    nome = models.CharField(max_length=30)

class Acessa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    permissao = models.CharField(max_length=15, choices=[
          ('Administrador','Administrador'),
          ('Cordenador','Cordenador'),
          ('Bolsista','Bolsista'),
          ('Visitante','Visitante'),
      ])
