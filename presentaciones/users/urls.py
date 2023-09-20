from django.urls import path
from . import views


urlpatterns = [
    path('', views.students, name='students'),
    path('perfil/', views.profile, name='profile'),
]