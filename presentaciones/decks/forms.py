from django import forms
from .models import Question, Choice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'image', 'data', 'form_type', 'question_set', 'topic']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'image': 'Imagen',
            'data': 'Datos',
            'form_type': 'Tipo de formulario',
            'question_set': 'Conjunto de preguntas',
            'topic': 'Tema',
        }
        placeholders = {
            'title': 'Escribe el título aquí',
            'description': 'Escribe la descripción aquí',
            'image': 'Selecciona una imagen',
            'data': 'Selecciona un archivo de datos',
        }
        help_texts = {}

        widgets = {
            'data': forms.ClearableFileInput(attrs={'accept': '.pdf, .doc, .docx, .txt, .jpg, .png'}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('title', css_class='mb-3'),
                Field('description', css_class='mb-3'),
                Field('image', css_class='mb-3'),
                Field('data', css_class='mb-3'),
                Field('form_type', css_class='mb-3'),
                Field('question_set', css_class='mb-3'),
                Field('topic', css_class='mb-3'),
                HTML('<hr class="mb-3">'),
            ),
        )
        self.fields['image'].required = False
        self.fields['data'].required = False
        self.fields['description'].widget.attrs['rows'] = 5
        for field_name, placeholder_text in self.Meta.placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
