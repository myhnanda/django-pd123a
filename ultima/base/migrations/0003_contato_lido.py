# Generated by Django 4.2.3 on 2023-08-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(default=False, verbose_name='Mensagem lida'),
        ),
    ]