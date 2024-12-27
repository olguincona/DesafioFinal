from django import forms
from .models import Comprador,Productos,Vendedor,Devolucion,Profile
from django.contrib.auth.models import User

class CompradorFormulario (forms.ModelForm):
    class Meta: 
        model = Comprador
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput (attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre del comprador"
            }),
            "apellido": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese la apellido del comprador"
            }),
            "email": forms.EmailInput (attrs={
                "class":"form-control", "placeholder": "Ingrese el email del comprador"
            })
        }

""" class ProductosFormulario (forms.ModelForm):
    class Meta: 
        model = Productos
        fields = "__all__"
        
        widgets = {
            "producto": forms.TextInput (attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre del producto"
            }),
            "unidades": forms.Textarea(attrs={
                "class":"form-control", "placeholder":"Ingrese la cantidad del producto"
            }),
            "precio": forms.Textarea (attrs={
                "class":"form-control", "placeholder": "Ingrese el precio del producto"
            })
        } """
class ProductosFormulario(forms.ModelForm):
    class Meta: 
        model = Productos
        fields = "__all__"
        
        widgets = {
            "producto": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ingrese el nombre del producto"
            }),
            "unidades": forms.NumberInput(attrs={
                "class": "form-control", "placeholder": "Ingrese la cantidad del producto"
            }),
            "precio": forms.NumberInput(attrs={
                "class": "form-control", "placeholder": "Ingrese el precio del producto"
            })
        }
class VendedorFormulario (forms.ModelForm):
    class Meta: 
        model = Vendedor
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput (attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre del vendedor"
            }),
            "apellido": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese la apellido del vendedor"
            }),
            "email": forms.EmailInput (attrs={
                "class":"form-control", "placeholder": "Ingrese el email del vendedor"
            }),
            "codigo": forms.NumberInput (attrs={
                "class":"form-control", "placeholder": "Ingrese el codigo del vendedor"
            })
        }

""" class DevolucionFormulario (forms.ModelForm):
    class Meta: 
        model = Devolucion
        fields = "__all__"
        
        widgets = {
            "producto": forms.TextInput (attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre del producto"
            }),
            "fechaDeEntrega": forms.DateInput(attrs={
                "class":"form-control", "placeholder":"Ingrese la fecha de devolucion del producto"
            }),
            "devuelto": forms.BooleanField ()
        } """

class DevolucionFormulario(forms.ModelForm):
    class Meta: 
        model = Devolucion
        fields = "__all__"
        
        widgets = {
            "producto": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ingrese el nombre del producto"
            }),
            "fechaDeEntrega": forms.DateInput(attrs={
                "class": "form-control", "placeholder": "Ingrese la fecha de devolución del producto",
                "type": "date"  # Esto mostrará un selector de fecha compatible con HTML5
            }),
            "devuelto": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            })
        }
        
class UserUpdateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ("first_name","last_name","email")

class UserProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ["photo"]