# Generated by Django 4.0.5 on 2022-06-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_alter_vehiculo_apellido_p_alter_vehiculo_cedula_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(upload_to='photos/photos'),
        ),
    ]
