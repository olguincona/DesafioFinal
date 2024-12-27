from django.db import models
from django.contrib.auth.models import User

class Productos (models.Model):
    producto = models.CharField(max_length=30)  
    unidades = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Nombre del Producto: {self.producto} - N° de Unidades: {self.unidades} - Precio del Producto: {self.precio}"

class Comprador (models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models. EmailField() 
    def __str__(self):
        return f"Nombre del Comprador: {self.nombre} - Apellido del Comprador: {self.apellido} - Email del Comprador: {self.email}"
    
class Vendedor (models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models. CharField(max_length=100)
    codigo = models.CharField(max_length=50) 
    def __str__(self):
        return f"Nombre del Vendedor: {self.nombre} - Apellido del Vendedor: {self.apellido} - Email del Vendedor: {self.email} - Codigo del Vendedor: {self.codigo}"

class Devolucion(models.Model):
    producto = models.CharField(max_length=100) 
    fechaDeEntrega = models.DateField() 
    devuelto = models. BooleanField() 
    def __str__(self):
        return f"Nombre del Producto: {self.producto} - Fecha de Devolucion: {self.fechaDeEntrega} - Devolucion {self.devuelto}"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photos/",null=True,blank=True)

    def __str__(self):
        return self.user.username