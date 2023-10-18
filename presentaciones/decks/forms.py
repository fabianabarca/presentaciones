from django import forms
from .models import Question, Choice
from django.forms import formset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'image', 'data', 'form_type', 'question_set', 'topic']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)

ChoiceFormSet = forms.modelformset_factory(
    Choice,
    form=ChoiceForm,
    extra=4,
    can_delete=True,
    max_num=10,
    validate_max=True
)
