# Generated by Django 4.2.3 on 2023-10-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0007_alter_reserva_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaanimal',
            name='nome',
            field=models.CharField(blank=True, choices=[('C', 'Cachorro'), ('G', 'Gato')], max_length=1, null=True),
        ),
    ]