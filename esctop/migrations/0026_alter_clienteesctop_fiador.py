# Generated by Django 3.2.6 on 2021-08-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_dadosdaempresa_options'),
        ('esctop', '0025_alter_clienteesctop_fiador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteesctop',
            name='fiador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais'),
        ),
    ]