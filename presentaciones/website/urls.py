from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.home, name='home'),
    path('anuncios/', views.anuncios, name='anuncios'),
    path('sobre/', views.about, name='about'),
    path('registro/', views.signup, name='signup'),
    path('ingreso/', views.login, name='login'),
    path('salida/', views.logout, name='logout'),
]