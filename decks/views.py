from django.shortcuts import get_object_or_404, render

# Create your views here.


def p2(request, deck_id):
    if request.user.is_staff:
        role = "presenter"
    else:
        role = "viewer"
    context = {"role": role}
    template = f"modelos/{deck_id}.html"
    return render(request, template, context)


def p4(request):
    if request.user.is_staff:
        role = "presenter"
    else:
        role = "viewer"
    context = {"role": role}
    return render(request, "modelos/4-variables-aleatorias.html", context)


def p15(request):
    if request.user.is_staff:
        role = "presenter"
    else:
        role = "viewer"
    context = {"role": role}
    return render(request, "modelos/15-caracteristicas-espectrales-procesos-estocasticos.html", context)


def p18(request):
    return render(request, "modelos/18-markov-tiempo-continuo.html")


def decks(request):
    return render(request, "decks.html")


def deck(request, deck_id):
    presentacion = "clases/" + str(deck_id) + ".html"
    context = {
        "presentacion": presentacion,
    }
    return render(request, "deck.html", context)


def websocket(request, deck_id):
    context = {
        "deck_id": deck_id,
    }
    return render(request, "websocket.html", context)


def master(request):
    context = {
        "deck_id": "master",
    }
    return render(request, "master.html", context)


def client(request):
    context = {
        "deck_id": "client",
    }
    return render(request, "client.html", context)
