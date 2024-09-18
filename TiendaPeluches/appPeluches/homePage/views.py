from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.shortcuts import render
from allauth.socialaccount.providers import registry
from creadorProductos.models import Categoria, Producto
from carro.carro import Carro


def home(request, categoria_slug=None):
    categorias = Categoria.objects.all()
    
    # Si no se selecciona una categoría, mostrar "top-ventas" por defecto
    if categoria_slug:
        categoria_actual = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categoria_actual)
    else:
        categoria_actual = Categoria.objects.get(slug='top-ventas')
        productos = Producto.objects.filter(categoria=categoria_actual)
    
    context = {
        'categorias': categorias,
        'productos': productos,
        'categoria_actual': categoria_actual,  # Se pasa la categoría actual a la plantilla
    }
    
    return render(request, 'homePage.html', context)


