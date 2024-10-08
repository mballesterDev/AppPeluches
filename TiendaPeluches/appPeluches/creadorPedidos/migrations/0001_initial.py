# Generated by Django 5.1 on 2024-08-27 09:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creadorProductos', '0003_producto_talla'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creadorProductos.producto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='creadorPedidos.pedido')),
            ],
        ),
    ]
