# Generated by Django 3.2.6 on 2021-08-12 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esctop', '0003_auto_20210812_0229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='razao_social',
            new_name='razaosocial',
        ),
    ]
