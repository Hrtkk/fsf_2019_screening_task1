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
    template_name = 'login.html'
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
            return redirect('/teams/createTeam')

        return redirect('/userAuth/signup')


class CustomSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/userAuth/'
    default_next = '/login'

    def post(self,request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()

        return redirect('/usersAuth/login')

class ProfileView(TemplateView):
    template_name = 'profile.html'
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

