from .models import Tasks
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django import forms

class CustomTaskCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['timestamp']