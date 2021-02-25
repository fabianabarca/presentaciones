from django.urls import path
from . import views

app_name = 'clases'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('semana<int:numero>', views.clase, name='clase'),
]