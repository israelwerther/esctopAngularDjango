# Generated by Django 3.2.6 on 2021-08-20 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
        ('core', '0010_alter_dadosdaempresa_options'),
        ('esctop', '0014_rename_dadosdaemresa_clienteesctop_dados_da_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteesctop',
            name='banco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='banco.banco', verbose_name='Banco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clienteesctop',
            name='dados_bancarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.dadosbancarios', verbose_name='Dados Bancários'),
            preserve_default=False,
        ),
    ]