# Generated by Django 3.2.6 on 2021-08-30 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esctop', '0038_alter_clienteesctop_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienteesctop',
            name='emprestimo',
        ),
        migrations.AddField(
            model_name='clienteesctop',
            name='emprestimos',
            field=models.ManyToManyField(to='esctop.EmprestimoEsctop', verbose_name='Emprestimos'),
        ),
    ]