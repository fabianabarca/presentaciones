from django.db import models

# Create your models here.

class RegistroUsuarios(models.Model):
    usuario = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
   

    def __str__(self):
        return self.usuario
