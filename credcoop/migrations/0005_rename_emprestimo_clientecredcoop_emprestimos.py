# Generated by Django 3.2.6 on 2021-08-27 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credcoop', '0004_auto_20210827_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientecredcoop',
            old_name='emprestimo',
            new_name='emprestimos',
        ),
    ]