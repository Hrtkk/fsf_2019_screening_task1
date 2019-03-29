from django.contrib.auth import get_user_model
from django import forms
MyUser = get_user_model()


class CustomSignupForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username')


class CustomLoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CustomLoginForm, self).__init__(*args, **kwargs)


