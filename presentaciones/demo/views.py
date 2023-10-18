from django.shortcuts import redirect, render
from decks.models import Question, Choice, Answer, Topic
from decks.forms import QuestionForm, ChoiceForm, ChoiceFormSet


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
            
        print(request.POST)
        # question_form = QuestionForm(request.POST, request.FILES)
        # choice_formset = ChoiceFormSet(request.POST, request.FILES, queryset=Choice.objects.none(), instance=Question())

        # if question_form.is_valid() and choice_formset.is_valid():
        #     question = question_form.save()
            
        #     for choice_form in choice_formset:
        #         if choice_form.cleaned_data.get('is_correct'):
        #             choice = choice_form.save()
        #             Answer.objects.create(question=question, user_id=1, choice=choice)

        return redirect('demo')  

    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet(queryset=Choice.objects.none())

    return render(request, 'questions_demo.html', {'question_form': question_form, 'choice_formset': choice_formset})
