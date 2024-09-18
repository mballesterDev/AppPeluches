from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Pedido, DetallePedido
from carro.context_processors import importe_total_carro
from creadorProductos.models import Producto
from decimal import Decimal
from carro.carro import Carro
from django.urls import reverse

def procesar_pedido(request):
    carro = Carro(request)
    
    if not carro.carro:
        return HttpResponse("No hay productos en el carrito.")
    
    if request.method == "POST":
        
        if request.user.is_authenticated:
            pedido = Pedido.objects.create(
                usuario=request.user,
                total=Decimal(sum(float(item["precio"]) for item in carro.carro.values())),
                pagado=False  # Ajusta esto según el estado del pago
            )
        else:
            pedido = Pedido.objects.create(
                total=Decimal(sum(float(item["precio"]) for item in carro.carro.values())),
                pagado=False
            )
            
        
        # Capturar los datos del formulario de entrega
        nombre_usuario = request.POST.get("nombre")
        direccion_usuario = request.POST.get("direccion")
        ciudad_usuario = request.POST.get("ciudad")
        cp_usuario = request.POST.get("CP")
        telefono_usuario = request.POST.get("telefono")
        correo_usuario = request.POST.get("email")
        
        # Crear los detalles del pedido
        for item in carro.carro.values():
            producto = get_object_or_404(Producto, id=item["id"])
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=item["cantidad"],
                talla=item["talla"],
                modelo = item["modelo"],
                precio=Decimal(item["precio"]),
                nombreUsario=nombre_usuario,
                direccionUsuario=direccion_usuario,
                ciudadUsuario=ciudad_usuario,
                CPUsuario=cp_usuario,
                telefonoUsuario=telefono_usuario,
                correoUsuario=correo_usuario
            )
        
        # Limpiar el carrito después de crear el pedido
        
        # Redirigir a una página de confirmación de pedido
        return redirect('pantalla_de_pago', pedido_id=pedido.id)

    return HttpResponse("Método no permitido", status=405)

def pantalla_de_pago(request, pedido_id):
    # Aquí ya obtienes el importe total del carrito correctamente
    importe_total = importe_total_carro(request)["importe_total_carro"]
    
    # Lo envías al template
    return render(request, 'pantalla_de_pago.html', { 'importe_total': importe_total, 'pedido_id': pedido_id })

def payment_success(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return render(request, 'payment_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def actualizar_pago(request, pedido_id):
    try:
        # Obtener el pedido por ID
        pedido = Pedido.objects.get(id=pedido_id)
        
        # Actualizar el estado de pagado
        pedido.pagado = True
        pedido.save()

        # Enviar correo electrónico de confirmación al usuario
        enviar_correo_confirmacion(pedido)

        # Redirigir a la página de éxito
        return redirect('payment_success')
    except Pedido.DoesNotExist:
        # Si el pedido no se encuentra, redirige a la página de error
        return HttpResponse("Pedido no encontrado.", status=404)

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def enviar_correo_confirmacion(pedido):
    # Asunto del email
    subject = 'Confirmación de tu pedido'

    # Renderizar el contenido del correo en HTML
    html_message = render_to_string('correo_confirmacion.html', {
        'pedido': pedido,
    })

    # Obtener el correo del primer detalle del pedido
    primer_detalle = pedido.detalles.first()
    
    # Verifica si existe al menos un detalle para obtener el correo del usuario
    if primer_detalle:
        recipient_list = [primer_detalle.correoUsuario]

        # Enviar el correo
        send_mail(
            subject,
            '',  # Puedes dejar el texto plano vacío si solo usas HTML
            settings.DEFAULT_FROM_EMAIL,  # Correo del remitente
            recipient_list,
            fail_silently=False,  # Si hay un error, Django lanza una excepción
            html_message=html_message  # Este es el contenido HTML
        )
