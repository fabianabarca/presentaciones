from django.db import models

# Create your models here.

class InfoProyecto(models.Model):
    objetivos = models.CharField(max_length=200)
    justificacion = models.CharField(max_length=200)
   

    def __str__(self):
        return self.objetivos
