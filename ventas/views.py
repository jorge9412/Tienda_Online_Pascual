from django.http import HttpResponse
from django.shortcuts import render
from inventario.models import Productos


def ventas_view(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

def guardar_venta(request,pk):
    producto = Productos.objects.get(id_producto=pk)
    if request.method == 'POST':
        
        producto.name = request.POST["nombre"]
        producto.category = request.POST["categoria"]
        producto.cost = request.POST["costo"]
        producto.cantidad_stock = request.POST["stock"]
        producto.description = request.POST["descripcion"]
        producto.save()
        return redirect('/mostrar_productos/')

    else:

        context = {
            'productos': producto,
        }

        return render(request,'guardarVenta.html',context)