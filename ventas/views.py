from django.http import HttpResponse
from django.shortcuts import render
from inventario.models import Productos


def ventas_view(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

