# Generated by Django 3.2.6 on 2021-08-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210811_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencia',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='referencia',
            name='endereco',
            field=models.CharField(blank=True, max_length=50, verbose_name='Parentesco'),
        ),
    ]
