from django.db import models
from django.contrib.auth.models import User
from courses.models import Career, Course

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    careers = models.ManyToManyField(Career)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"