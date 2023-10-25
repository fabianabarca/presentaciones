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
                    is_correct_key = f'is_correct_{key.split("_")[1]}'

                    # Verificar si esta opción es la correcta
                    is_correct = is_correct_key in request.POST

                    # Crear y guardar la opción en la base de datos
                    choice = Choice(question_id=question, text=choice_text, is_correct=is_correct)
                    choice.save()
                    choices.append(choice)

            # Si se necesita una respuesta, puedes crearla aquí
            # answer = Answer(question_id=question, user_id=1, choice_id=choices[0])
            # answer.save()

            return redirect('demo')

    else:
        question_form = QuestionForm()

    return render(request, 'questions_demo.html', {'question_form': question_form})


# def create_question(request):
#     if request.method == 'POST':
            
#         print(request.POST)
#         question_form = QuestionForm(request.POST, request.FILES)
#         choice_formset = ChoiceFormSet(request.POST, request.FILES, queryset=Choice.objects.none())

#         if question_form.is_valid() and choice_formset.is_valid():
#             print("Is valid")
#             question = question_form.save()
            
#             for choice_form in choice_formset:
#                 if choice_form.cleaned_data.get('is_correct'):
#                     choice = choice_form.save()
#                     Answer.objects.create(question=question, user_id=1, choice=choice)
        
#         else:
#             print("El formulario no es valido")

#         return redirect('demo')

#     else:
#         question_form = QuestionForm()
#         # Corrección: No se utiliza 'instance' en ChoiceFormSet
#         choice_formset = ChoiceFormSet(queryset=Choice.objects.none())

#     return render(request, 'questions_demo.html', {'question_form': question_form, 'choice_formset': choice_formset})

