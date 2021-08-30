# Generated by Django 3.2.6 on 2021-08-30 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0003_auto_20210827_0447'),
        ('esctop', '0039_auto_20210830_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienteesctop',
            name='emprestimos',
        ),
        migrations.AddField(
            model_name='clienteesctop',
            name='emprestimos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimo.emprestimo', verbose_name='Emprestimos'),
        ),
        migrations.DeleteModel(
            name='EmprestimoEsctop',
        ),
    ]