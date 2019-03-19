from .models import Teams
from django import forms
from django.contrib.auth import get_user_model

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

