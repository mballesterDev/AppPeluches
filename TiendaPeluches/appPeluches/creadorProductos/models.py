from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, allow_unicode=True)  # Para crear URLs amigables

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requeireTalla = models.BooleanField(default=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    tamanyo1 = models.CharField(max_length=100, blank=True, null=True)
    tamanyo2 = models.CharField(max_length=100, blank=True, null=True)
    tamanyo3 = models.CharField(max_length=100, blank=True, null=True)
    tamanyo4 = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    
    # Hacemos que las imágenes sean opcionales
    imagen = models.ImageField(upload_to='productos', default='default.jpg')
    imagen2 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen4 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen5 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagen6 = models.ImageField(upload_to='productos', blank=True, null=True)
    imagenEXTRA = models.ImageField(upload_to='productos', blank=True, null=True)
    
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    
    categoria = models.ManyToManyField('Categoria', related_name='productos')
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")



    def save(self, *args, **kwargs):    
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nombre



class FotoUsuario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='fotos_usuario')
    imagen = models.ImageField(upload_to='fotosUsuarios')
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.producto.nombre} - {self.id}"


