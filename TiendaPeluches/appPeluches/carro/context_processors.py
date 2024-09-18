# carro/context_processors.py

from decimal import Decimal

def format_price(value):
    """
    Esta función formatea el valor de precio para que use un punto decimal
    en lugar de una coma, que es lo que espera PayPal u otros sistemas.
    """
    return f"{Decimal(value):.2f}"

def importe_total_carro(request):
    total = Decimal("3.00")  # Envío por defecto con Decimal
    
    # Verifica si existe el carrito en la sesión
    carrito = request.session.get("carro", {})  # Si no existe, devuelve un diccionario vacío
    
    # Recorre los productos del carrito
    for key, value in carrito.items():
        total += Decimal(value["precio"])  # Suma el precio del producto al total usando Decimal

    # Si el total es mayor que 40€, elimina el costo de envío
    if total >= Decimal("20.00"):
        total -= Decimal("3.00")  # Restar el envío
    
    # Asegúrate de devolver el total con el formato adecuado
    return {"importe_total_carro": format_price(total),
            "importe_total_carro_raw": total}

def carrito_context(request):
    total_productos = 0
    
    # Verifica si existe el carrito en la sesión
    carrito = request.session.get("carro", {})  # Si no existe, devuelve un diccionario vacío
    
    # Suma las cantidades de los productos en el carrito
    for key, value in carrito.items():
        total_productos += int(value["cantidad"])

    return {"total_productos": total_productos}
