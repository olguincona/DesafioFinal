from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.template import Template, Context, loader
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Productos,Vendedor,Comprador,Devolucion,Profile
from .forms import ProductosFormulario,VendedorFormulario,CompradorFormulario,DevolucionFormulario,UserUpdateForm,UserProfileForm
def inicio(request):
    return render(request,"WebApp/index.html")

def show_profile(request):
    return render(request,"WebApp/forms/show-profile.html")

def edit_profile(request):
    usuario = request.user
    profile, _=Profile.objects.get_or_create(user=usuario)

    if request.method == "POST":

        user_form = UserUpdateForm(request.POST,instance=usuario)
        profile_form = UserProfileForm(request.POST, request.FILES,instance=profile )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect ("perfil")
        else:
            return redirect ("inicio")
    else:
        user_form = UserUpdateForm(instance=usuario)
        profile_form = UserProfileForm(instance=profile)
    return render(request,"WebApp/forms/edit-profile.html", {"user_form":user_form,"profile_form":profile_form})

def change_password(request):
    usuario = request.user
    if request.method == "POST":
        form_password = PasswordChangeForm (usuario, request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request,usuario)
            return redirect ("perfil")
        else:
            return redirect ("inicio") 
    else:
        form_password = PasswordChangeForm (usuario)
    return render(request,"WebApp/forms/change-password.html",{"form_password":form_password})

 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ("inicio")
        else:
            return redirect ("inicio")
    else:
        return render(request, "WebApp/forms/login.html")

def user_logout(request):
    logout(request)
    return redirect ("login")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("login")
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, "WebApp/forms/register.html",{"form":form})


def productos(request): 
    query = request.GET.get("q")
    if query:
        productos = Productos.objects.filter(Q(producto__icontains=query) | Q(unidades__icontains=query) | Q(precio__icontains=query))
    else:
        productos = Productos.objects.all()

    if request.method == "POST":
        new_producto = Productos(producto=request.POST["producto"], unidades=request.POST["unidades"], precio=request.POST["precio"])
        print('se hizo post')
        new_producto.save()
        productos = Productos.objects.all()
    return render(request, "WebApp/productos.html", {"productos": productos})

@login_required(login_url='login')
def vendedores(request):
    query = request.GET.get("q")
    if query:
        vendedores = Vendedor.objects.filter((Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(codigo__icontains=query)))
    else:
        vendedores = Vendedor.objects.all()
    if request.method == "POST":
        vendedores = Vendedor(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],codigo=request.POST["codigo"])
        print('se hizo post')
        vendedores.save()
        vendedores = Vendedor.objects.all()
    return render(request,"WebApp/vendedores.html",{"vendedores": vendedores})

@login_required(login_url='login')
def compradores(request):
    query = request.GET.get("q")
    if query:
        compradores = Comprador.objects.filter((Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query)))
    else:
        compradores = Comprador.objects.all()
    if request.method == "POST":
        compradores = Comprador(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"])
        print('se hizo post')
        compradores.save()
        compradores = Comprador.objects.all()
    return render(request,"WebApp/compradores.html",{"compradores": compradores})

@login_required(login_url='login')
def devoluciones(request):
    query = request.GET.get("q")
    if query:
        devoluciones = Devolucion.objects.filter((Q(producto__icontains=query) | Q(fechaDeEntrega__icontains=query) | Q(devuelto=query.lower() in ["true", "1", "on"])))
    else:
        devoluciones = Devolucion.objects.all()
    if request.method == "POST":
        devuelto = request.POST.get("devuelto") == "on"
        devoluciones = Devolucion(producto=request.POST["producto"],fechaDeEntrega=request.POST["fechaDeEntrega"],devuelto=devuelto)
        print('se hizo post')
        devoluciones.save()
        devoluciones = Devolucion.objects.all()
    return render(request,"WebApp/devoluciones.html",{"devoluciones": devoluciones})


def formulario_producto(request):
    if request.method == "POST":
        new_producto = Productos(producto=request.POST["producto"], unidades=request.POST["unidades"], precio=request.POST["precio"])
        print('se hizo post')
        new_producto.save()
        #return render(request,"WebApp/forms/formulario_Producto.html")
        return redirect("productos")
    else:
        return render(request,"WebApp/forms/formulario_producto.html")
    

class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Productos
    template_name = "WebApp/vbc/productos-vbc-crear.html"
    fields = "__all__"
    success_url = reverse_lazy('productos')

class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    model = Productos
    template_name = "WebApp/vbc/productos-vbc-eliminar.html"
    success_url = reverse_lazy('productos')


class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model = Productos
    template_name = "WebApp/vbc/productos-vbc-editar.html"
    success_url = reverse_lazy('productos')
    fields = "__all__"

class CompradorCreateView(LoginRequiredMixin,CreateView):
    model = Comprador
    template_name = "WebApp/vbc/productos-vbc-crear.html"
    fields = "__all__"
    success_url = reverse_lazy('compradores')

class CompradorDeleteView(LoginRequiredMixin,DeleteView):
    model = Comprador
    template_name = "WebApp/vbc/productos-vbc-eliminar.html"
    success_url = reverse_lazy('compradores')


class CompradorUpdateView(LoginRequiredMixin,UpdateView):
    model = Comprador
    template_name = "WebApp/vbc/productos-vbc-editar.html"
    success_url = reverse_lazy('compradores')
    fields = "__all__"

class VendedorCreateView(LoginRequiredMixin,CreateView):
    model = Vendedor
    template_name = "WebApp/vbc/vendedores-vbc-crear.html"
    fields = "__all__"
    success_url = reverse_lazy('vendedores')

class VendedorDeleteView(LoginRequiredMixin,DeleteView):
    model = Vendedor
    template_name = "WebApp/vbc/vendedores-vbc-eliminar.html"
    success_url = reverse_lazy('vendedores')


class VendedorUpdateView(LoginRequiredMixin,UpdateView):
    model = Vendedor
    template_name = "WebApp/vbc/vendedores-vbc-editar.html"
    success_url = reverse_lazy('vendedores')
    fields = "__all__"


class DevolucionCreateView(LoginRequiredMixin,CreateView):
    model = Devolucion
    template_name = "WebApp/vbc/devoluciones-vbc-crear.html"
    fields = "__all__"
    success_url = reverse_lazy('devoluciones')

class DevolucionDeleteView(LoginRequiredMixin,DeleteView):
    model = Devolucion
    template_name = "WebApp/vbc/devoluciones-vbc-eliminar.html"
    success_url = reverse_lazy('devoluciones')


class DevolucionUpdateView(LoginRequiredMixin,UpdateView):
    model = Devolucion
    template_name = "WebApp/vbc/devoluciones-vbc-editar.html"
    success_url = reverse_lazy('devoluciones')
    fields = "__all__"
    