from django.contrib import admin
from .models import Pedido, DetallePedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_pedido', 'total', 'pagado')
    list_filter = ('pagado', 'fecha_pedido')
    search_fields = ('usuario__username', 'total')
    date_hierarchy = 'fecha_pedido'
    ordering = ('-fecha_pedido',)
    list_display_links = ('usuario',)  # Asegúrate de que 'id' es clicable

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad','talla','modelo', 'precio','direccionUsuario', 'ciudadUsuario', 'CPUsuario', 'telefonoUsuario', 'correoUsuario')
    list_filter = ('pedido', 'producto')
    search_fields = ('pedido__id', 'producto__nombre')
    ordering = ('pedido', 'producto')
