from .models import Articls
from django.forms import ModelForm, TextInput, Textarea



class ArticlesForm(ModelForm):
    class Meta:
        model = Articls
        fields = ['title', 'text_state']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':  'название статьи'
            }),
            "text_state": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'название статьи'
            }),

        }