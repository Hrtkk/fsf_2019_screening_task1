from .models import Teams
from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import Tasks

User = get_user_model()


class CustomTeamCreationForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    date = forms.DateTimeField(required=False)

    class Meta:
        model = Teams
        fields = ['title', 'description']


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


