# Generated by Django 4.2.1 on 2023-10-18 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_avaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.categoriaanimal'),
            preserve_default=False,
        ),
    ]
