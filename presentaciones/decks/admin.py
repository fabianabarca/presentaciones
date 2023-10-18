from django.contrib import admin
from .models import Question, Choice, Answer, Topic

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Topic)
