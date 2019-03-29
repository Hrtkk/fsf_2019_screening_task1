from django.views.generic import CreateView, TemplateView, View, RedirectView, FormView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render_to_response, render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout as auth_logout, REDIRECT_FIELD_NAME, login as auth_login
from django.contrib import auth
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from .forms import CustomSignupForm,CustomLoginForm
from .admin import UserCreationForm
from .mixins import NextUrlMixin, RequestFormAttachMixin
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .mixins import AjaxFormMixin


class CustomLoginView(LoginView,NextUrlMixin, RequestFormAttachMixin):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            # print("Hey you are logged in")
            return HttpResponseRedirect('/teams/')

        return redirect('/')


class CustomSignupView(AjaxFormMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/teams/'
    success_message = 'User registered successfully'

    def post(self,request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        # print(request.POST)
        print('request to create user')
        if form.is_valid():
            print("Form is valid")
            form.save()
            return HttpResponseRedirect('/teams/')
        else :
            messages.error(request, "Error")
        return render_to_response(self.template_name,{'form':form})
    
   

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'
    context = {
        'hello':'data'
    }

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name,self.context)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'index.html'

