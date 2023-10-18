from django.db import models

# Modelos
class Topic(models.Model):
    topic_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.topic_id}. {self.name}"
    
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    data = models.FileField(null=True)
    form_type = models.CharField(max_length=255)
    question_set = models.CharField(max_length=255) #?
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Foreing Key

    def __str__(self):
        return self.title


class Choice(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Respuesta a la pregunta {self.question_id} por el usuario {self.user_id}"

