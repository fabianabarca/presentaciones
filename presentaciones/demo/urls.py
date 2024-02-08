from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.demo, name="demo"),
    path("programacion/", views.programming, name="programming"),
    path("visualizaciones/", views.visualizations, name="visualizations"),
    path("ecuaciones/", views.equations, name="equations"),
    path("interactividad/", views.interactivity, name="interactivity"),
    path("ejemplo/", views.example, name="example"),
    path("maestra/", views.master, name="master"),
    path("cliente/", views.client, name="client"),
    path('crear_pregunta/', views.create_question, name='create_question'),
]
