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
          ('adm','Administrador'),
          ('cord','Cordenador'),
          ('bols','Bolsista'),
          ('vist','Visitante'),
      ])

class Animal(models.Model):
    codigo = models.IntegerField(primary_key=True)
    peso = models.DecimalField(max_digits=5 , decimal_places=2)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    especie = models.CharField(max_length=10, choices=[
        ('C','Caprino'),
        ('O','Ovino')
    ])  
    sexo = models.CharField(max_length=10 , choices=[
          ('F','Fêmea'),
          ('M','Macho')
      ])
    data_nascimento = models.DateField()
    pelagem = models.CharField(max_length=50)
    registro = models.DateField()

class Material(models.Model):  
    tipo = models.CharField(max_length=30, choices=[
        ('med','Medicamento'),
        ('equip','Equipamento Veterinário'),
        ('limp','Material de Limpeza')
        ])
    nome = models.CharField(max_length=30, primary_key=True)
    quantidade = models.IntegerField()
    validade = models.DateField()

class Doenca(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)    

class VincularDoenca(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
    dataregistro = models.DateField()

class SaidaAnimal(models.Model):
    codigo = models.IntegerField()
    motivo = models.TextField(max_length=500)  
    saida = models.DateField()