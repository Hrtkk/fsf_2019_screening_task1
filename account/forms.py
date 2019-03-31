from django.contrib.auth import get_user_model
from django import forms
MyUser = get_user_model()


class CustomSignupForm(forms.ModelForm):
    """
    Custom signup form
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username')


class CustomLoginForm(forms.Form):
    """ Custom Login Form """
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        """ constructor to initialize form with request data, arguments and keyword arguments. """
        self.request = request
        super(CustomLoginForm, self).__init__(*args, **kwargs)


