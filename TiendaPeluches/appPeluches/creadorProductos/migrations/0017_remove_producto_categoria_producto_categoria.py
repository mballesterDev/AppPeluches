# Generated by Django 5.1 on 2024-09-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorProductos', '0016_producto_imagenextra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(related_name='productos', to='creadorProductos.categoria'),
        ),
    ]
