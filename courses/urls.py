from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courses, name='cursos'),
    path('<str:id>/', views.course),
    path('<str:id>/temas/', include('decks.urls')),
]
