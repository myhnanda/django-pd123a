# Generated by Django 4.2.3 on 2023-10-04 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_petshop_alter_reserva_porte'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservas', to='reserva.petshop'),
        ),
    ]
