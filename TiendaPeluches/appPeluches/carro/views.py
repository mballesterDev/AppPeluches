from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from  creadorProductos.models import Producto
from .carro import Carro  # Asegúrate de que la ruta del import sea correcta


from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render



def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    
    talla = request.POST.get('talla')  # Obtiene la talla del formulario
    modelo = request.POST.get('modelo')  # Obtiene el modelo del formulario
    messages.success(request, 'El producto fue añadido al carrito.')
    # Instancia el carrito y agrega el producto con talla y modelo
    carro = Carro(request)
    carro.agregar(producto, talla, modelo)  # Pasa la talla y el modelo al método agregar
    
    
    return redirect('producto_detalle', slug=producto.slug)


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = Carro(request)
    carro.eliminar(producto)
    return redirect('carro:carrito')
    

def restar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = Carro(request)
    carro.restar(producto)
    return redirect('carro:carrito')
   

def limpiar_carrito(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('carro:carrito')
    

def ver_carrito(request):
    carro = Carro(request)
    productos = carro.carro.items()  # Usa items() si deseas obtener un iterable de (clave, valor)
    return render(request, 'carrito.html', {'productos': productos})
    