# Generated by Django 5.1 on 2024-09-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorProductos', '0005_producto_requierefotos_fotousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fotoUser1',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fotoUser2',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fotoUser3',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fotoUser4',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fotoUser5',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
        migrations.AddField(
            model_name='producto',
            name='fotoUser6',
            field=models.ImageField(blank=True, upload_to='fotosUsuarios'),
        ),
    ]
