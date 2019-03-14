from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bootstrap_modal_forms.mixins import PassRequestMixin, LoginAjaxMixin
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usersAuth/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('Teams:teamsView')


class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'usersAuth/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')
