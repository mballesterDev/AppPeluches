class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro", {})

    def agregar(self, producto, talla=None, modelo=None):
    # Obtener el precio basado en la talla seleccionada
        if talla == producto.tamanyo2:
            precio = float(producto.precio2)
        elif talla == producto.tamanyo3:
            precio = float(producto.precio3)
        elif talla == producto.tamanyo4:
            precio = float(producto.precio4)
        else:
            precio = float(producto.precio)  # Precio base, por defecto

        producto_id = str(producto.id)

        if producto_id not in self.carro:
            # Inicializar el carrito para el nuevo producto
            self.carro[producto_id] = {
                "id": producto.id,
                "nombre": producto.nombre,
                "talla": talla if talla else "",  # Si no hay talla, inicializar con cadena vacía
                "modelo": modelo if modelo else "",  # Si no hay modelo, inicializar con cadena vacía
                "precio": str(precio),  # Usar el precio correcto basado en la talla
                "cantidad": 1,
                "slug": producto.slug,
                "imagen": producto.imagen.url
            }
        else:
            # Si ya existe en el carrito, actualizar la cantidad y el precio
            item = self.carro[producto_id]
            item["cantidad"] += 1
            item["precio"] = str(float(item["precio"]) + precio)
            
            # Añadir la talla a la lista de tallas, incluso si ya existe
            if talla:
                if item["talla"]:
                    item["talla"] += f", {talla}"
                else:
                    item["talla"] = talla
            
            # Añadir el modelo a la lista de modelos, incluso si ya existe
            if modelo:
                if item["modelo"]:
                    item["modelo"] += f", {modelo}"
                else:
                    item["modelo"] = modelo

        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)

        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar(self, producto):
        producto_id = str(producto.id)

        if producto_id in self.carro:
            item = self.carro[producto_id]
            if item["cantidad"] > 0:
                # Obtener la última talla añadida
                tallas = item["talla"].split(', ')
                ultima_talla = tallas[-1] if tallas else None

                # Obtener el precio basado en la última talla seleccionada
                if ultima_talla == producto.tamanyo2:
                    precio = float(producto.precio2)
                elif ultima_talla == producto.tamanyo3:
                    precio = float(producto.precio3)
                elif ultima_talla == producto.tamanyo4:
                    precio = float(producto.precio4)
                else:
                    precio = float(producto.precio)  # Precio base, por defecto

                # Restar una unidad del producto
                item["cantidad"] -= 1
                item["precio"] = str(float(item["precio"]) - precio)
                
                # Si la cantidad es 0 o menos, eliminar el producto
                if item["cantidad"] < 1:
                    self.eliminar(producto)
                else:
                    # Actualizar las tallas eliminando la última talla
                    if item["talla"]:
                        tallas.pop()  # Elimina la última talla
                        item["talla"] = ', '.join(tallas)  # Vuelve a unir las tallas restantes

                    # Actualizar los modelos si se ha restado una unidad
                    if item["modelo"]:
                        modelos = item["modelo"].split(', ')
                        modelos.pop()  # Elimina el último modelo
                        item["modelo"] = ', '.join(modelos)  # Vuelve a unir los modelos restantes

                self.guardar_carro()

    
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
