from django.db import models

# Create your models here.
        
class Plantas(models.Model):
    especie = models.CharField(max_length=30, primary_key=True)
    tipo = models.CharField(max_length=30)
    producao = models.IntegerField()
    doacao = models.IntegerField()
    venda = models.IntegerField()
    extravio = models.IntegerField()
    ifrn = models.IntegerField()

    def __str__(self):
        return self.especie
    
    class Meta:
        verbose_name = "planta"
        verbose_name_plural = 'plantas'
        
class Insumos(models.Model):
    cod = models.IntegerField(primary_key=True, default="0")
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    desc = models.TextField()
    quant = models.IntegerField()

    def __str__(self):
        return self.desc
    
    class Meta:
        verbose_name = "insumo"
        verbose_name_plural = 'insumos'
                            
class Visitas(models.Model):
    cod = models.IntegerField(primary_key=True, default="0")
    data = models.DateField()
    hora = models.TimeField(max_length=30)
    visitante = models.TextField()

    def __str__(self):
        return self.visitante
    
    class Meta:
        verbose_name = "visita"
        verbose_name_plural = 'visitas'