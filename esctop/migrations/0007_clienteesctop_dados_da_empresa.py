# Generated by Django 3.2.6 on 2021-08-12 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dadosdaempresa_razao_social'),
        ('esctop', '0006_auto_20210812_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteesctop',
            name='dados_da_empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.dadosdaempresa', verbose_name='empresinha'),
            preserve_default=False,
        ),
    ]
