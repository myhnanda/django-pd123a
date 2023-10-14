# Generated by Django 4.2.3 on 2023-10-14 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_reserva_data_reserva_alter_reserva_porte_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField()),
                ('petshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.petshop')),
            ],
        ),
    ]
