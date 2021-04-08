from django.db import models
# Create your models here.

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