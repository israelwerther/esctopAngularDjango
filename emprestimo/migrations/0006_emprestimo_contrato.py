# Generated by Django 3.2.6 on 2021-08-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0005_remove_emprestimo_contrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='contrato',
            field=models.CharField(max_length=50, null=True, verbose_name='Contrato'),
        ),
    ]
