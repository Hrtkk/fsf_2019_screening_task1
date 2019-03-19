from django.views.generic import CreateView, TemplateView, View, RedirectView, FormView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render_to_response, render
from django.contrib.auth import logout as auth_logout, REDIRECT_FIELD_NAME, login as auth_login
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator

# from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CustomSignupForm,CustomLoginForm
from .admin import UserCreationForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'usersAuth/login.html'
    success_url = '/'
    default_next = '/'
    # redirect_field_name = REDIRECT_FIELD_NAME

    def post(self, request, *args, **kwargs):
        print(request.POST)
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(request,username=username, password=password)
        # print(email, password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("Hey you are logged in")
            # Redirect to a success page.
            request.session['username'] = username
            return redirect('/teams/')

        return redirect('/')


class CustomSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'usersAuth/signup.html'
    success_url = '/teams/'
    default_next = '/teams/'

    def post(self,request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()

        return redirect('/teams')

class ProfileView(TemplateView):
    template_name = 'usersAuth/profile.html'
    context = {
        'hello':'data'
    }

    def get(self, request, *args, **kwargs):
        print(request.GET)
        print("I am in session")
        print(request.session.keys())
        print(request.session['username'])
        return render_to_response(self.template_name,self.context)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class IndexView(TemplateView):
    template_name = 'index.html'

