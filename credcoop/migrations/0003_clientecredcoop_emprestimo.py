# Generated by Django 3.2.6 on 2021-08-22 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_emprestimo_funcionario'),
        ('credcoop', '0002_clientecredcoop_dados_bancarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientecredcoop',
            name='emprestimo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emprestimo.emprestimo', verbose_name='Emprestimos'),
            preserve_default=False,
        ),
    ]
