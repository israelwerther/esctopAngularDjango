# Generated by Django 3.2.6 on 2021-08-21 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_dadosdaempresa_options'),
        ('esctop', '0023_auto_20210821_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteesctop',
            name='fiador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais'),
            preserve_default=False,
        ),
    ]
