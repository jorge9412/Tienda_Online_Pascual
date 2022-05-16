from django.http import HttpResponse
from django.shortcuts import render

from login.forms_login import Login

def ventas_view(request):
    return render (request, "ventas.html")

