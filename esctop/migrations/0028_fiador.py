# Generated by Django 3.2.6 on 2021-08-27 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
        ('core', '0013_auto_20210827_0527'),
        ('esctop', '0027_clienteesctop_emprestimo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.banco', verbose_name='Banco')),
                ('contatos', models.ManyToManyField(to='core.Contato', verbose_name='Contatos')),
                ('dados_bancarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadosbancarios', verbose_name='Dados Bancários')),
                ('dados_pessoais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais')),
                ('enderecos', models.ManyToManyField(to='core.Endereco', verbose_name='Endereço')),
            ],
        ),
    ]