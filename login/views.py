from distutils.log import Log
from django.shortcuts import render
from django.http import HttpResponse
from login.forms_login import Login

# Create your views here.


def login_app(request):

    if request.method=="POST":

        login_form = Login(request.POST)

        if login_form.is_valid():
                
            obtener_datos = login_form.cleaned_data
            return HttpResponse(str(obtener_datos))        
    
    else:

        login_form = Login()

        return render (request, "login_app.html", {"form": login_form})