from django.db import models

# Create your models here.

class Contacto(models.Model):
    id_contacto = models.CharField(primary_key = True, max_length=50 , default="")
    asunto = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.CharField(max_length=200)

