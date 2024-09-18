
from django.shortcuts import get_object_or_404, render
from creadorProductos.models import Categoria, Producto

def categoria_detalle(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()  # Todas las categorías para el menú o enlaces
    
    context = {
        'categoria': categoria,  # La categoría actual
        'productos': productos,  # Los productos de la categoría actual
        'categorias': categorias,  # Todas las categorías
    }
    return render(request, 'categoria_detalle.html', context)


def productos_view(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    context = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'productos.html', context)


def producto_detalle(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    context = {
        
        'producto': producto,
    }
    return render(request, 'producto_detalle.html', context)


def search (request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Producto.objects.filter(nombre__icontains=searched)
        return render(request, 'base.html', {'searched': searched})
    else:
        return render(request, 'base.html', {})
    