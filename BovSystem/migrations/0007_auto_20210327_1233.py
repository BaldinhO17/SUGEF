# Generated by Django 3.1.7 on 2021-03-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BovSystem', '0006_auto_20210327_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobertura',
            name='femea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='femea', to='BovSystem.animal'),
        ),
        migrations.AlterField(
            model_name='cobertura',
            name='macho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='macho', to='BovSystem.animal'),
        ),
        migrations.AlterField(
            model_name='entrada_saida_estoque',
            name='gasto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BovSystem.registro_financeiro'),
        ),
        migrations.AlterField(
            model_name='gravidez',
            name='cobertura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BovSystem.cobertura'),
        ),
        migrations.AlterField(
            model_name='nascimento',
            name='matriz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriz', to='BovSystem.animal'),
        ),
        migrations.AlterField(
            model_name='nascimento',
            name='pai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pai', to='BovSystem.animal'),
        ),
        migrations.AlterField(
            model_name='saida_leite',
            name='ganho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BovSystem.registro_financeiro'),
        ),
        migrations.AlterField(
            model_name='secacao',
            name='matriz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BovSystem.animal'),
        ),
    ]
