# Generated by Django 5.1.2 on 2024-10-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_rename_serial_carroceria_vehiculo_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_modificacion',
            field=models.DateField(null=True),
        ),
    ]
