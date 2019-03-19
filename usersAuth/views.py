from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib import auth
# from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CustomSignupForm,CustomLoginForm
from .admin import UserCreationForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'usersAuth/login.html'
    success_url = '/userAuth/profile'
    default_next = '/userAuth/profile'

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

        return redirect('/userAuth/signup')


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


class IndexView(TemplateView):
    template_name = 'index.html'

