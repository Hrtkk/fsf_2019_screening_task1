from .models import Teams
from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import Tasks, Comments

User = get_user_model()


class CustomTeamCreationForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    date = forms.DateTimeField(required=False)

    class Meta:
        model = Teams
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomTeamCreationForm, self).__init__(*args, **kwargs)
        # print(self.request.user)
        mem = User.objects.exclude(username = self.request.user.username)
        self.fields['members'].queryset = mem


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments']


CHOICES = (
    ('Planned', 'Planned'),
    ('Progressing', 'Progressing'),
    ('Done', 'Done'),
)


class CustomTaskCreateForm(forms.ModelForm):
    Assigned =  forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)
    class Meta:
        model = Tasks
        fields = ['title','description','status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.team = kwargs.pop('team',None)
        super(CustomTaskCreateForm, self).__init__(*args, **kwargs)
        if self.request.method == 'GET':
            self.TM1 = self.team.teamMember.all()
            self.TM2 = User.objects.filter(username = self.request.user.username)     
            self.fields['Assigned'].queryset = self.TM1

