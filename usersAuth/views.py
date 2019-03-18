from django.shortcuts import render, render_to_response,HttpResponse, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    TemplateView,
)
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from .mixins import NextUrlMixin, RequestFormAttachMixin
from django.views.decorators.csrf import csrf_protect
from .forms import CustomLoginForm, CustomSignupForm


# Create your views here.

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'usersAuth/login.html'
    success_url = '/'
    default_next = '/'
    # def get(self, request, *args, **kwargs):
    #     # context = super().get_context_data()
    #     # context['form'] = self.form_class
    #
    #     return render(request,self.template_name,{'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # print(request.COOKIES['csrftoken'])
        # print(request.POST.get('csrfmiddlewaretoken'))
        #
        # # if form.is_valid():
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(email, password)
        user = auth.authenticate(email=email, password=password)
        if user is not None and user.is_active:
        #     # request.session['']
        #     # Correct password, and the user is marked "active"
            auth.login(request, user)
            print("Hey you are logged in")
            self.user = user
            # Redirect to a success page.
            return redirect('/')

            # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            # Show an error page
            return HttpResponseRedirect("/usersAuth/signup/")


class CustomSignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'usersAuth/signup.html'
    success_url = '/'
    default_next = '/'

class IndexView(TemplateView):
    template_name = 'index.html'


    # def get(self, request, *args, **kwargs):

    #     return

    # def post(self, request, *args, **kwargs):

    #     return