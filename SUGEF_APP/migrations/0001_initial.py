# Generated by Django 3.1.7 on 2021-04-06 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Acessa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao', models.CharField(choices=[('Administrador', 'Administrador'), ('Cordenador', 'Cordenador'), ('Bolsista', 'Bolsista'), ('Visitante', 'Visitante')], max_length=15)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SUGEF_APP.setor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SUGEF_APP.usuario')),
            ],
        ),
    ]
