from django.urls import path, include
from . import views  # Asegúrate de que esto sea correcto


app_name = 'carro'  
urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    
    
    
]
