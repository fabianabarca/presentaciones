from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.demo, name="demo"),
    path("proyecto/", views.project, name="project"),
    path("programacion/", views.programming, name="programming"),
    path("visualizaciones/", views.visualizations, name="visualizations"),
    path("ecuaciones/", views.equations, name="equations"),
    path("interactividad/", views.interactivity, name="interactivity"),
    path("ejemplo/", views.example, name="example"),
]
