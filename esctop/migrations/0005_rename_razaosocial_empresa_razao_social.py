# Generated by Django 3.2.6 on 2021-08-12 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esctop', '0004_rename_razao_social_empresa_razaosocial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='razaosocial',
            new_name='razao_social',
        ),
    ]