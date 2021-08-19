# Generated by Django 3.2.6 on 2021-08-12 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_dadosdaempresa'),
        ('esctop', '0002_auto_20210812_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representante',
            name='contatos',
        ),
        migrations.RemoveField(
            model_name='representante',
            name='enderecos',
        ),
        migrations.AlterField(
            model_name='representante',
            name='dados_pessoais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais', verbose_name='Dados pessoais'),
        ),
    ]
