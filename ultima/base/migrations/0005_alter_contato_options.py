# Generated by Django 4.2.3 on 2023-08-28 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_contato_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data', 'lido'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contato'},
        ),
    ]
