from django.shortcuts import redirect, render
from decks.models import Question, Choice, Answer
from django.http import JsonResponse

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
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                choice_id = request.POST[key]

                question = Question.objects.get(pk=question_id)
                choice = Choice.objects.get(pk=choice_id)

                is_correct = choice.is_correct

                # Guarda la respuesta del usuario en la base de datos
                answer = Answer(question_id=question, user_id=request.user.id, choice_id=choice)
                answer.save()
                
        return JsonResponse({
            'message': 'Respuesta correcta',
            'is_correct': is_correct
        })


    else:
        question_sets = {}
        questions = Question.objects.all()

        for question in questions:
            if question.question_set not in question_sets:
                question_sets[question.question_set] = []

            choices = Choice.objects.filter(question_id=question)
            question_sets[question.question_set].append({'question': question, 'choices': choices})

        return render(request, "interactivity.html", {'question_sets': question_sets})


def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)

        if question_form.is_valid():
            # Guarda la pregunta
            question = question_form.save()

            # Procesa las opciones enviadas en el request
            choices = []
            for key, value in request.POST.items():
                if key.startswith("choices__"):
                    choice_text = value
                    is_correct_key = f'is_correct_{key.split("_")[2]}'

                    # Verifica si esta opción es la correcta
                    is_correct = is_correct_key in request.POST

                    choice = Choice(question_id=question, text=choice_text, is_correct=is_correct)
                    choice.save()
                    choices.append(choice)

            return redirect('demo')

    else:
        question_form = QuestionForm()

    return render(request, 'questions_demo.html', {'question_form': question_form})

