from django.contrib import admin
from decks.models import Choice, Session, Question, Answer, Topic

# Register your models here.
admin.site.register(Choice)
admin.site.register(Session)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
