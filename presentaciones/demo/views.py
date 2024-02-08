import json
from django.shortcuts import redirect, render
from decks.models import Question, Choice, Answer
from django.http import JsonResponse

from decks.forms import QuestionForm


def demo(request):
    return render(request, "demo.html")


def project(request):
    return render(request, "project.html")


def programming(request):
    return render(request, "programming.html")


def visualizations(request):
    return render(request, "visualizations.html")


def equations(request):
    return render(request, "equations.html")


def example(request):
    return render(request, "example.html")

def master(request):
    return render(request, "maestra.html")

def client(request):
    return render(request, "cliente.html")


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
        # Fetch questions and choices
        questions = Question.objects.all()
    
        # Convert questions and their choices to dictionaries
        question_sets = {}
        for question in questions:
            if question.question_set not in question_sets:
                question_sets[question.question_set] = []

            choices = Choice.objects.filter(question_id=question)
            choices_data = [{'choice_id': choice.choice_id, 'text': choice.text, 'is_correct': choice.is_correct} for choice in choices]
            question_data = {
                'question_id': question.question_id,
                'title': question.title,
                'description': question.description,
                'choices': choices_data
            }
            question_sets[question.question_set].append(question_data)

        # Serialize the dictionary to JSON
        question_sets_json = json.dumps(question_sets)

        # Other parts of your view...

        return render(request, "interactivity.html", {'question_sets_json': question_sets_json})


def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        print(request.POST)
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

