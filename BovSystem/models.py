from django.db import models

# Create your models here.


class Animal(models.Model):
    codigo = models.IntegerField(primary_key=True)
    peso = models.DecimalField(max_digits=5 , decimal_places=2)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30, default='Bovino')
    sexo = models.CharField(max_length=10 , choices=[
          ('Feminino','Feminino'),
          ('Masculino','Masculino')
      ])

class Registro_Financeiro(models.Model):
    descricao = models.TextField(blank=True, default='')
    valor = models.DecimalField(max_digits=5 , decimal_places=2)
    data = models.DateField()
    hora = models.TimeField()


class Produc_leite(models.Model):
    
    data = models.DateField()
    quantidade = models.DecimalField(max_digits=5 , decimal_places=2)
    femea = models.ForeignKey(Animal, on_delete=models.CASCADE)

class Saida_Leite(models.Model):
    
    data = models.DateField()
    quantidade = models.IntegerField()
    destino = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=30)
    ganho = models.ForeignKey(Registro_Financeiro, on_delete=models.CASCADE, blank=True, null=True)


class Cobertura(models.Model):
    inicio = models.DateField()
    macho = models.ForeignKey(Animal, related_name='macho' , on_delete=models.CASCADE)
    femea = models.ForeignKey(Animal, related_name='femea' , on_delete=models.CASCADE)
    ativa = models.BooleanField(default=True)
    termino = models.DateField(blank = True, null = True)

class Gravidez(models.Model):
    inicio = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)
    ativa = models.BooleanField(default=True)
    termino = models.DateField(blank = True, null = True)

class Nascimento(models.Model):
    data = models.DateField()
    pai = models.ForeignKey(Animal, related_name='pai' ,on_delete=models.CASCADE)
    matriz = models.ForeignKey(Animal, related_name='matriz' , on_delete=models.CASCADE)
    filhote = models.ForeignKey(Animal, on_delete=models.CASCADE)
    peso_nasc = models.DecimalField(max_digits=5 , decimal_places=2)
#    obito = models.BooleanField()

class Material(models.Model):
    tipo = models.CharField(max_length=30, choices=[
        ('Medicamento','Medicamento'),
        ('Equipamento Veterinário','Equipamento Veterinário'),
        ('Material de Limpeza','Material de Limpeza')
        ])
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    # quant_un = models.DecimalField(max_digits=5 , decimal_places=2)
    # un_medida = models.CharField(max_length=3, choices=[
    #     ('l','l'),
    #     ('ml','ml'),
    #     ('g','g'),
    #     ('mg','mg')
    #     ])
    validade = models.DateField()

class Entrada_Saida_Estoque(models.Model):
    tipo = models.CharField(max_length=10 , choices=[
        ('Entrada','Entrada'),
        ('Saida','Saida')
    ])
    descricao = models.TextField()
    gasto = models.ForeignKey(Registro_Financeiro, on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateField()
    hora = models.TimeField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Secacao(models.Model):
    
    inicio = models.DateField()
    matriz = models.ForeignKey(Animal, on_delete=models.CASCADE)
    leite = models.CharField(max_length=30, choices=[
        ('NÃO MAIS','NÃO MAIS'),
        ('POUCO LEITE','POUCO LEITE'),
        ('MUITO LEITE','MUITO LEITE')
        ])
    ativa = models.BooleanField(default=True)
    termino = models.DateField(blank = True, null = True)

