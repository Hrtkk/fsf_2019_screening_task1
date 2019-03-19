from django import forms
from .models import Tasks


class Comments(forms.ModelForm):
    author = forms.CharField(max_length=255)
    comments = forms.CharField(max_length=255)


CHOICES = (
    ('Planned', 'Planned'),
    ('Progressing', 'Progressing'),
    ('Done', 'Done'),
)


class CustomTaskCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','description','status']


