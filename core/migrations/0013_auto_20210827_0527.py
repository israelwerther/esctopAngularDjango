# Generated by Django 3.2.6 on 2021-08-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210827_0523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencia',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='referencia',
            name='parentesco',
            field=models.CharField(blank=True, max_length=50, verbose_name='Parentesco'),
        ),
    ]
