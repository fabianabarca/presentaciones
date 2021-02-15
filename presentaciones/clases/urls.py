from django.urls import path
from . import views

app_name = 'clases'

url_patterns = [
    path('', views.clase, name='class'),
]