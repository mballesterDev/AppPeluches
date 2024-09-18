from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Asegúrate de que las vistas importadas sean correctas
from homePage import views as views_home
from creadorProductos import views as views_productos
from carro import views as views_carro  # Alias específico para las vistas de carro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_home.home, name='home'),  # Vista de la página de inicio desde homePage
    path('productos/', views_productos.productos_view, name='productos'),  # Vista de productos desde creadorProductos
    path('categoria/<slug:slug>/', views_productos.categoria_detalle, name='categoria_detalle'),  # Vista de categoría desde creadorProductos
    path('producto/<slug:slug>/', views_productos.producto_detalle, name='producto_detalle'),  # Vista de detalle del producto
    path('accounts/', include('allauth.urls')),  # Rutas de autenticación
    path('carro/', include('carro.urls')),  # Incluye las URLs del carrito desde carro.urls
    path('pedidos/', include('creadorPedidos.urls')),  # Incluye las URLs de pedidos desde creadorPedidos
    path('search/', views_productos.search, name='search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
