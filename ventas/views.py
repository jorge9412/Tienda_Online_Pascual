from django.http import HttpResponse
from django.shortcuts import redirect, render
from inventario.models import Productos
from ventas.models import Venta


def ventas_view(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

def guardar_venta(request,pk): 
    producto = Productos.objects.get(id_producto=pk)
    if request.method == 'POST':        
        id = producto.id_producto
        nombreCom = request.POST["txt_nombres"]
        tipoDoc = request.POST["select_tipo_doc"]
        numDoc = request.POST["txt_num_doc"]
        correoDoc = request.POST["txt_correo"]
        direccionDoc = request.POST["txt_direccion"]
        deptoDoc = request.POST["select_depto"]
        ciudadDoc = request.POST["select_ciudad"]
        telefonoDoc = request.POST["txt_telefono"]

        #producto.cantidad_stock = request.POST[stok]
        data = Venta(nombres=nombreCom, tipo_doc=tipoDoc, num_doc=numDoc, 
                            correo= correoDoc, direccion=direccionDoc,depto=deptoDoc,ciudad=ciudadDoc,
                            telefono=telefonoDoc,id_producto_id = id ,total_venta=0)
        data.save()
        producto.cantidad_stock -= 1
        producto.save()             
        return redirect('ventas')

    else:
        context = {
        'productos': producto,
        }
        return render(request,'guardarVenta.html',context)
    