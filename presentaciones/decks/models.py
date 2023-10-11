from django.db import models

# Create your models here.

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    equation = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=255)
    set = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Choice(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()  # Cambia esto según tu implementación de usuarios
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Respuesta a la pregunta {self.question_id} por el usuario {self.user_id}"
