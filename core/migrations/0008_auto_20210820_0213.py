# Generated by Django 3.2.6 on 2021-08-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dadosdaempresa_razao_social'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dadosbancarios',
            options={'verbose_name': 'Dado Bancário', 'verbose_name_plural': 'Dados Bancários'},
        ),
        migrations.AlterModelOptions(
            name='dadosdaempresa',
            options={'verbose_name_plural': 'Razão '},
        ),
        migrations.AlterField(
            model_name='dadosdaempresa',
            name='razao_social',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Razão Social'),
        ),
    ]
