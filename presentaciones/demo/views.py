from django.shortcuts import redirect, render
from decks.models import Question, Choice, Answer, Topic
from decks.forms import QuestionForm


def demo(request):
    return render(request, "demo.html")


def programming(request):
    return render(request, "programming.html")


def visualizations(request):
    return render(request, "visualizations.html")


def equations(request):
    return render(request, "equations.html")


def example(request):
    return render(request, "example.html")


def interactivity(request):
    return render(request, "interactivity.html")


def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)

        if question_form.is_valid():
            # Guardar la pregunta
            question = question_form.save()

            # Procesar las opciones enviadas en el request
            choices = []
            for key, value in request.POST.items():
                if key.startswith("choices__"):
                    choice_text = value
                    is_correct_key = f'is_correct_{key.split("_")[2]}'

                    # Verificar si esta opción es la correcta
                    is_correct = is_correct_key in request.POST

                    # Crear y guardar la opción en la base de datos
                    choice = Choice(question_id=question, text=choice_text, is_correct=is_correct)
                    choice.save()
                    choices.append(choice)

            # answer = Answer(question_id=question, user_id=1, choice_id=choices[0])
            # answer.save()

            return redirect('demo')

    else:
        question_form = QuestionForm()

    return render(request, 'questions_demo.html', {'question_form': question_form})

