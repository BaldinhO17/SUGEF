from django import forms
from .models import Animal, Nascimento, Cobertura, Gravidez, Produc_leite, Saida_Leite, Secacao, Registro_Financeiro, Material, Entrada_Saida_Estoque

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['codigo', 'nome', 'sexo', 'peso', 'raca']

class NascimentoForm(forms.ModelForm):
    class Meta:
        model = Nascimento
        fields = ['data', 'pai', 'matriz', 'filhote', 'peso_nasc']

class CoberturaForm(forms.ModelForm):
    class Meta:
        model = Cobertura
        fields = ['id', 'inicio', 'femea', 'macho']

class SecacaoForm(forms.ModelForm):
    class Meta:
        model = Secacao
        fields = ['id', 'inicio', 'matriz', 'leite']

class GravidezForm(forms.ModelForm):
    class Meta:
        model = Gravidez
        fields = ['id', 'inicio', 'animal','cobertura']

class Produc_leiteForm(forms.ModelForm):
    class Meta:
        model = Produc_leite
        fields = ['id', 'data', 'quantidade','femea']

class Saida_LeiteForm(forms.ModelForm):
    class Meta:
        model = Saida_Leite
        fields = ['id', 'data', 'quantidade','destino','responsavel']

class Registro_FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Registro_Financeiro
        fields = ['id', 'descricao', 'valor','data','hora']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['id','nome', 'tipo', 'quantidade','validade']

class Entrada_Saida_EstoqueForm(forms.ModelForm):
    class Meta:
        model = Entrada_Saida_Estoque
        fields = ['id', 'tipo', 'descricao','gasto','material','quantidade','data','hora']