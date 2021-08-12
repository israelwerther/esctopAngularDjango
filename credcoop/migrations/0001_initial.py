# Generated by Django 3.2.6 on 2021-08-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_dadosbancarios'),
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteCredcoop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.banco', verbose_name='Banco')),
                ('contatos', models.ManyToManyField(to='core.Contato', verbose_name='Contatos')),
                ('dados_pessoais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dadospessoais', verbose_name='Dados pessoais')),
                ('enderecos', models.ManyToManyField(to='core.Endereco', verbose_name='Endereços')),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.referencia')),
            ],
            options={
                'verbose_name': 'Cliente Credcoop',
                'verbose_name_plural': 'Clientes Credcoop',
            },
        ),
    ]
