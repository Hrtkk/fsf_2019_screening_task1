from .models import Team
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django import forms

class CustomTeamCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Team
        exclude = ['timestamp']