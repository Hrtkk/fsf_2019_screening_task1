from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.views import LoginView
from django.utils.http import is_safe_url
from .views import CustomLoginView

User = get_user_model()

class CustomSignupForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(CustomSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit:
            user.save()
        return user



class CustomLoginForm(forms.Form):
    email = forms.CharField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = request
        email = data.get("email")
        password = data.get("password")
        qs = User.objects.filter(email=email)
        # if qs.exists():
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credential")
        login(request, user)
        self.user = user
        return data


    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")

        print(self.user)
        if self.user is not None:
            if not self.user.is_active:
                print('inactive user..')
                messages.success(request, "This user is inactive")
                return super(LoginView, self).form_invalid(form)
            login(request, self.user)
            user_logged_in.send(self.user.__class__, instance=self.user, request=request)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(CustomLoginView, self).form_invalid(form)


    # class Meta:
    #     model = User
    #     fields = ['email', 'password']
