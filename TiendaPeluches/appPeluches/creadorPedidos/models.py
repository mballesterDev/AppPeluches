from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pedido(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="pedidos")
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.total} €"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey('creadorProductos.Producto', on_delete=models.CASCADE)  # Actualiza con el nombre correcto de la app
    cantidad = models.PositiveIntegerField()
    talla = models.CharField(max_length=10, default="N/A")
    modelo = models.CharField(max_length=10, default="N/A")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombreUsario = models.CharField(max_length=100, default="ninguno")
    direccionUsuario = models.CharField(max_length=100, default="ninguno")
    ciudadUsuario = models.CharField(max_length=100, default="ninguno")
    CPUsuario = models.CharField(max_length=100, default="ninguno")
    telefonoUsuario = models.CharField(max_length=100, default="ninguno")
    correoUsuario = models.CharField(max_length=100, default="ninguno")
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - {self.precio} €"

