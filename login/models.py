from django import forms
from django.db import models

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
