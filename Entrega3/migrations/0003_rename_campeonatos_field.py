# Generated by Django 5.2.3 on 2025-07-17 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega3', '0002_rename_puntos_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campeones',
            old_name='Campeonatos',
            new_name='campeonatos',
        ),
    ]
