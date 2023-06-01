from django.urls import path
from . import views

app_name = 'clases'

urlpatterns = [
    path('', views.decks, name='temas'),
    path('<slug:slug>', views.deck, name='tema'),
]