from django.db import models

# Create your models here.

# TODO: Crear el modelo de carreras


class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=31)
    name = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Career(models.Model):
    id = models.CharField(primary_key=True, max_length=31)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
