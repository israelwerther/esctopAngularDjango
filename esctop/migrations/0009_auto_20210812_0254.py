# Generated by Django 3.2.6 on 2021-08-12 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dadosdaempresa_razao_social'),
        ('esctop', '0008_alter_clienteesctop_dados_da_empresa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empresa',
            new_name='DadosDaEmpresa',
        ),
        migrations.AlterField(
            model_name='clienteesctop',
            name='dados_da_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadosdaempresa'),
        ),
    ]
