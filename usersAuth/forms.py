# Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth import get_user_model


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
