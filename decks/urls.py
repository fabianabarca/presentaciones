from django.urls import path
from . import views

urlpatterns = [
    path("", views.decks, name="temas"),
    path("websocket/<slug:deck_id>/", views.websocket, name="websocket"),
    path("maestra/", views.master, name="master"),
    path("cliente/", views.client, name="client"),
    path("proyecto-programacion/", views.programming_project, name="programming_project"),
    path("hola/<slug:deck_id>", views.deck, name="tema"),
    path("teorema-bayes", views.p2, name="teorema-bayes"),
    path("variables-aleatorias", views.p4, name="variables-aleatorias"),
    path("caracteristicas-espectrales", views.p15, name="caracteristicas-espectrales"),
    path("markov-tiempo-continuo", views.p18, name="markov-tiempo-continuo"),
    path("markov-tiempo-continuo-vector-estado-estable", views.p19, name="markov-tiempo-continuo-vector-estado-estable"),
]
