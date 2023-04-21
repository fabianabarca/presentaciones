from django.db import models

# Create your models here.

class CreadorDemos(models.Model):
    multimedia = models.CharField(max_length=200)
    interactividad = models.CharField(max_length=200)
   

    def __str__(self):
        return self.multimedia
