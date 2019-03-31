from .models import Teams
from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import Tasks, Comments

User = get_user_model()


class CustomTeamCreationForm(forms.ModelForm):
    """  Team creation form """
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    date = forms.DateTimeField(required=False)

    class Meta:             
        # Meta data for form data, field from model Team to be displayed while creating teams
        model = Teams
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        # constructor to populating form with the keywords arguments of forms
        self.request = kwargs.pop('request', None)
        super(CustomTeamCreationForm, self).__init__(*args, **kwargs)
        # print(self.request.user)
        # Excluding user from form list to choose as member to simplify database
        mem = User.objects.exclude(username = self.request.user.username)
        self.fields['members'].queryset = mem           # queryset for team members


class CommentsForm(forms.ModelForm):
    class Meta:
        # Metadata for comments 
        model = Comments
        fields = ['comments']


CHOICES = (
    ('Planned', 'Planned'),
    ('Progressing', 'Progressing'),
    ('Done', 'Done'),
)


class CustomTaskCreateForm(forms.ModelForm):
    # extra field for assigning task to team members
    Assigned =  forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)
    
    class Meta:
        # meta data for form to render
        model = Tasks
        fields = ['title','description','status']

    def __init__(self, *args, **kwargs):
        # constructor to populate form with data coming from post request
        self.request = kwargs.pop('request', None)
        self.team = kwargs.pop('team',None)
        super(CustomTaskCreateForm, self).__init__(*args, **kwargs)
        if self.request.method == 'GET':
            # showing only those members in assigned portion of form 
            # which are team members
            self.TM1 = self.team.teamMember.all()
            self.TM2 = User.objects.filter(username = self.request.user.username)     
            self.fields['Assigned'].queryset = self.TM1

