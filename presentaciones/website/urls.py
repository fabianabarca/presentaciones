from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='ejemplo'),
    path('inicio/', views.inicio, name='inicio'),
    path('anuncios/', views.anuncios, name='anuncios'),
]