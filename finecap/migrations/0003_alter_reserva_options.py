# Generated by Django 4.2.5 on 2023-09-20 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finecap', '0002_reserva_data_reserva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ['data_reserva']},
        ),
    ]