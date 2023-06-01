from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courses, name='cursos'),
    path('<str:sigla>/', views.course),
    path('<str:sigla>/temas/', include('decks.urls')),
]
