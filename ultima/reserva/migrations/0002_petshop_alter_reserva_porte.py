# Generated by Django 4.2.3 on 2023-10-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Petshop',
                'verbose_name_plural': 'Petshops',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterField(
            model_name='reserva',
            name='porte',
            field=models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')]),
        ),
    ]
