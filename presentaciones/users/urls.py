from django.urls import path
from . import views
from .views import profile, signup, login, logout


urlpatterns = [
    path('perfil/', views.profile, name='perfil'),
    path('registro/', views.signup, name='registro'),
    path('ingreso/', views.login, name='ingreso'),
    path('logout/', views.logout, name='logout'),
]