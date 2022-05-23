from django.http import HttpResponse
from django.shortcuts import redirect, render
from inventario.models import Productos
from ventas.models import Venta


def ventas_view(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

def guardar_venta(request,pk):
    producto = Productos.objects.get(id_producto=pk) 
    context = {
        'productos': producto,
    }
    return render(request,'guardarVenta.html',context)

def guardar_venta2(request): 
 
    if request.method == 'POST':        
        id = request.POST["id"]
        nombreCom = request.POST["txt_nombres"]
        tipoDoc = request.POST["select_tipo_doc"]
        numDoc = request.POST["txt_num_doc"]
        correoDoc = request.POST["txt_correo"]
        direccionDoc = request.POST["txt_direccion"]
        deptoDoc = request.POST["select_depto"]
        ciudadDoc = request.POST["select_ciudad"]
        telefonoDoc = request.POST["txt_telefono"]
        totalVenta = request.POST["cos"]
        data = Venta(nombres=nombreCom, tipo_doc=tipoDoc, num_doc=numDoc, 
                            correo= correoDoc, direccion=direccionDoc,depto=deptoDoc,ciudad=ciudadDoc,
                            telefono=telefonoDoc,id_producto_id = id ,total_venta=totalVenta)
        data.save()
        return redirect('/ventas/')

    else:
        return render (request, "ventas.html")