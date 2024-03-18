from django.utils import timezone
import uuid
from django.shortcuts import render
from decks.models import Session

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def project(request):
    if request.user.is_staff:
        role = "presenter"
    else:
        role = "viewer"
    context = {"role": role}
    return render(request, "project.html", context)


def programming(request):
    return render(request, "programming.html")


def visualizations(request):
    return render(request, "visualizations.html")


def equations(request):
    return render(request, "equations.html")


def example(request):
    return render(request, "example.html")


def interactivity(request):
    user_id = request.user.id
    if request.user.is_staff:
        role = "presenter"
        deck_id = str(uuid.uuid4())
        # Crear una nueva sesión
        new_session = Session.objects.create(
            presenter_id=user_id, deck_id=deck_id, begins_at=timezone.now()
        )
        print(new_session.session_id)
        new_session.save()
        context = {
            "role": role,
            "session_id": new_session.session_id,
            "user_id": user_id,
        }
    else:
        role = "viewer"
        context = {"role": role, "user_id": user_id, "session_id": "8"}
    # context = {"role": role}
    return render(request, "interactivity.html", context)
