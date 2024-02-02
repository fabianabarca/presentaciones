from django.urls import path
from . import views
from users.views import profile

urlpatterns = [
    path('', views.index, name='index'), # Site
    path('inicio/', views.home, name='home'), # Platform
    path('anuncios/', views.anuncios, name='anuncios'),
    path('sobre/', views.about, name='about'),
    path('registro/', views.signup, name='signup'),
    path('ingreso/', views.login, name='login'),
    path('salida/', views.logout, name='logout'),
    path('perfil/', profile, name='profile'),
]