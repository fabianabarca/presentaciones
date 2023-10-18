from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Choice, Answer
from .forms import QuestionForm, ChoiceForm 

# Create your views here.

def decks(request):
    return render(request, 'decks.html')

def deck(request, slug):
    presentacion = 'clases/' + str(slug) + '.html'
    context = {
        'presentacion': presentacion,
    }
    return render(request, 'deck.html', context)


def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        choice_formset = ChoiceFormSet(request.POST, prefix='choices')
        
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save()
            for choice_form in choice_formset:
                if choice_form.cleaned_data:
                    text = choice_form.cleaned_data['text']
                    is_correct = choice_form.cleaned_data['is_correct']
                    choice = Choice(question=question, text=text, is_correct=is_correct)
                    choice.save()
            
            return redirect('decks')
            
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet(prefix='choices')
        
    return render(request, 'questions.html', {'question_form': question_form, 'choice_formset': choice_formset})
