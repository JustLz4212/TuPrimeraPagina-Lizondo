# Generated by Django 5.2.3 on 2025-06-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piloto',
            name='escuderia',
        ),
        migrations.AlterField(
            model_name='campeones',
            name='Campeonatos',
            field=models.IntegerField(),
        ),
    ]
