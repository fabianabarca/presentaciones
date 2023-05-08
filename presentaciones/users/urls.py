from django.urls import path
from . import views
from .views import registro,login,logout_usuario


urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.login, name='ingreso'),
    path('logout_usuario/', views.logout_usuario, name='logout_usuario'),
]