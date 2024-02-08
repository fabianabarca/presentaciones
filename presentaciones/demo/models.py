from django.db import models

# Create your models here.


class Snippet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    code = models.TextField()
    output = models.CharField(max_length=100)

    def __str__(self):
        return self.name
