# Generated by Django 3.2.6 on 2021-08-20 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esctop', '0011_alter_clienteesctop_dados_da_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representante',
            name='dados_pessoais',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Representante',
        ),
    ]
