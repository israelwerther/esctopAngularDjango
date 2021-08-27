# Generated by Django 3.2.6 on 2021-08-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_dadosdaempresa_options'),
        ('esctop', '0029_alter_fiador_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fiador',
            options={'verbose_name': 'Fiador', 'verbose_name_plural': 'Fiadores'},
        ),
        migrations.AlterField(
            model_name='clienteesctop',
            name='enderecos',
            field=models.ManyToManyField(related_name='_esctop_clienteesctop_enderecos_+', to='core.Endereco'),
        ),
        migrations.AlterField(
            model_name='clienteesctop',
            name='fiador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esctop.fiador', verbose_name='Fiador'),
        ),
        migrations.AlterField(
            model_name='fiador',
            name='dados_bancarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadosbancarios', verbose_name='Dados Bancários do faiador'),
        ),
        migrations.AlterField(
            model_name='fiador',
            name='dados_pessoais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais', verbose_name='Dados pessoais'),
        ),
        migrations.AlterField(
            model_name='fiador',
            name='enderecos',
            field=models.ManyToManyField(related_name='_esctop_fiador_enderecos_+', to='core.Endereco'),
        ),
    ]
