# Generated by Django 3.2.6 on 2021-08-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_dadosdaempresa_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencia',
            name='endereco',
        ),
        migrations.AddField(
            model_name='referencia',
            name='enderecos',
            field=models.CharField(blank=True, max_length=50, verbose_name='Endereço'),
        ),
    ]
