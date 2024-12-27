from django.urls import path
from WebApp import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('register/',views.register_view,name="register"),

    path('perfil/',views.show_profile,name="perfil"),
    path('perfil/editar',views.edit_profile,name="perfil-editar"),
    path('perfil/change-password',views.change_password,name="change-password"),

    path('about-us',views.aboutus,name="acerca"),


    #Productos
    path('productos/',views.productos,name="productos"),
    path('productos-vbc/crear',views.ProductoCreateView.as_view(),name="productos-vbc-crear"),
    path('productos-vbc/eliminar/<int:pk>',views.ProductoDeleteView.as_view(),name="productos-vbc-eliminar"),
    path('productos-vbc/editar/<int:pk>',views.ProductoUpdateView.as_view(),name="productos-vbc-editar"),

    #Compradores
    path('compradores/',views.compradores,name="compradores"), 
    path('compradores-vbc/crear',views.CompradorCreateView.as_view(),name="compradores-vbc-crear"),
    path('compradores-vbc/eliminar/<int:pk>',views.CompradorDeleteView.as_view(),name="compradores-vbc-eliminar"),
    path('compradores-vbc/editar/<int:pk>',views.CompradorUpdateView.as_view(),name="compradores-vbc-editar"),

    #Vendedores
    path('vendedores/',views.vendedores,name="vendedores"),
    path('vendedores-vbc/crear',views.VendedorCreateView.as_view(),name="vendedores-vbc-crear"),
    path('vendedores-vbc/eliminar/<int:pk>',views.VendedorDeleteView.as_view(),name="vendedores-vbc-eliminar"),
    path('vendedores-vbc/editar/<int:pk>',views.VendedorUpdateView.as_view(),name="vendedores-vbc-editar"),

    #Devoluciones
    path('devoluciones/',views.devoluciones,name="devoluciones"),
    path('devoluciones-vbc/crear',views.DevolucionCreateView.as_view(),name="devoluciones-vbc-crear"),
    path('devoluciones-vbc/eliminar/<int:pk>',views.DevolucionDeleteView.as_view(),name="devoluciones-vbc-eliminar"),
    path('devoluciones-vbc/editar/<int:pk>',views.DevolucionUpdateView.as_view(),name="devoluciones-vbc-editar"),

    path('formulario_producto/',views.formulario_producto,name="formulario_producto"),
]





