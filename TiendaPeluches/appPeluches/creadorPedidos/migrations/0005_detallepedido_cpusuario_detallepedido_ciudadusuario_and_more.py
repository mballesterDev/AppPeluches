# Generated by Django 5.1 on 2024-09-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorPedidos', '0004_remove_detallepedido_comentarios_fotos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepedido',
            name='CPUsuario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='ciudadUsuario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='correoUsuario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='direccionUsuario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='nombreUsario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='telefonoUsuario',
            field=models.CharField(default='ninguno', max_length=100),
        ),
    ]
