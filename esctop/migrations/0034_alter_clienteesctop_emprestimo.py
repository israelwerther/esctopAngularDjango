# Generated by Django 3.2.6 on 2021-08-27 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0003_auto_20210827_0447'),
        ('esctop', '0033_alter_clienteesctop_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteesctop',
            name='emprestimo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimo.emprestimo', verbose_name='Emprestimos'),
        ),
    ]
