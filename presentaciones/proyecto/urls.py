from django.urls import path
from . import views

app_name = 'proyecto'

urlpatterns = [
    path('', views.proyecto, name='proyecto'),
]