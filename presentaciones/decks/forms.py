from django import forms
from .models import Question, Choice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Submit

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
            'title': forms.TextInput(attrs={'class': 'mb-3'}),
            'description': forms.Textarea(attrs={'class': 'mb-3', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'mb-3'}),
            'data': forms.ClearableFileInput(attrs={'class': 'mb-3', 'accept': '.pdf, .doc, .docx, .txt, .jpg, .png'}),
            'form_type': forms.TextInput(attrs={'class': 'mb-3'}),
            'question_set': forms.TextInput(attrs={'class': 'mb-3'}),
            'topic': forms.Select(attrs={'class': 'mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['data'].required = False
        self.fields['description'].widget.attrs['rows'] = 5
        for field_name, placeholder_text in self.Meta.placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
