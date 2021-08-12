# Generated by Django 3.2.6 on 2021-08-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='numero',
            field=models.CharField(max_length=50, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='whatsapp',
            field=models.BooleanField(default=False, verbose_name='É whatsapp?'),
        ),
    ]