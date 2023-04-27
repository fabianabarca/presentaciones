from django.db import models

# Create your models here.

class Sesion(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()
    numero = models.PositiveIntegerField(primary_key=True)
    tema = models.PositiveIntegerField(help_text="Uno de los grandes temas del curso.")

    def __str__(self):
        return str(self.numero) + ' - ' + self.nombre