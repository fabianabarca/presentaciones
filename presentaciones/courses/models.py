from django.db import models

# Create your models here.


class Course(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
