from django.urls import path, include 
from . import views






urlpatterns = [
    # Otras URLs...
    path('procesar-pedido/', views.procesar_pedido, name='procesar_pedido'),
    path('paypal', include('paypal.standard.ipn.urls')),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('pantalla_de_pago/<int:pedido_id>/', views.pantalla_de_pago, name='pantalla_de_pago'),
    path('actualizar_pago/<int:pedido_id>/', views.actualizar_pago, name='actualizar_pago'),
]
