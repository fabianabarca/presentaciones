from django.urls import path
from . import views
from users.views import profile

urlpatterns = [
    path('', views.index, name='index'), # Site (without login)
    path('inicio/', views.home, name='home'), # Platform (with login)
    path('anuncios/', views.announcements, name='announcements'),
    path('sobre/', views.about, name='about'),
    path('registro/', views.signup, name='signup'),
    path('ingreso/', views.login, name='login'),
    path('salida/', views.logout, name='logout'),
    path('perfil/', profile, name='profile'),
]