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
    """
        customizing the login process by rendering custom login form
    """
    form_class = CustomLoginForm                # login form
    template_name = 'registration/login.html'   # login template to be rendered

    def post(self, request, *args, **kwargs):
        # post method which will accept the post request of the given form when user will click lohin button of form
        # print(request.POST)
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)         # extracting user from database if uer is available it will return user object otherwise will return None
      
        if user is not None:
            auth.login(request, user)           # django buildin auth.login method for log a user in 
            request.session['username'] = username          # putting username in user session
            return HttpResponseRedirect('/teams/')          # redirecting user to /teams/

        return redirect('/')


class CustomSignupView(AjaxFormMixin, CreateView):
    """ Custom signup view class """
    form_class = UserCreationForm           
    template_name = 'registration/signup.html'
    success_url = '/teams/'
    success_message = 'User registered successfully'

    def post(self,request, *args, **kwargs):
        # post method of the class to handle post request by user during signing up
        form = UserCreationForm(request.POST)
        if form.is_valid():     # checking form validity
            form.save()
            return HttpResponseRedirect('/home/')
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
    """ Log a user out and refirecting him to home page """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'index.html'

