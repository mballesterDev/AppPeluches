from django.contrib import admin
from .models import Categoria, Producto, FotoUsuario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio','precio2','precio3','precio4','modelo', 'requeireTalla', 'mostrar_categorias', 'slug', 'tamanyo1', 'tamanyo2', 'tamanyo3', 'tamanyo4', 'imagen', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'imagen6', 'video')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion')
    list_display_links = ('nombre',)  # Asegúrate de que 'nombre' es clicable



    def mostrar_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categoria.all()])
    
    mostrar_categorias.short_description = 'Categorías'
@admin.register(FotoUsuario)
class FotoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'fecha', 'imagen')


