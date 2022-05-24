"""tienda_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from inventario.views import editar_producto, eliminar_producto, mostrar_productos, vista_busqueda_productos, obtener_producto, agregar_producto, mostrar_productos, editar_producto, eliminar_producto
from contacto.views import mensaje_contacto
from login.views import login_app
from ventas.views import guardar_venta, guardar_venta2, ventas_view
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', vista_busqueda_productos),
    path('obtener_producto/', obtener_producto),
    path('agregar_producto/', agregar_producto,name='add-prods'),
    path('mostrar_productos/', mostrar_productos, name='show-prods'),
    path('editar_producto/<int:pk>', editar_producto, name='edit-prods'),
    path('eliminar_producto/<int:pk>', eliminar_producto, name="del-prods"),
    path('contacto/', mensaje_contacto),
    path('login/', login_app),
    path('guardarVenta/<int:pk>', guardar_venta),
    path('guardarVenta2/', guardar_venta2),
    path('ventas/', ventas_view),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

