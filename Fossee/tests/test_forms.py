from django.test import TestCase
from account.forms import CustomLoginForm, CustomSignupForm
from Teams.forms import CustomTaskCreateForm, CustomTeamCreationForm, CommentsForm
from django.http import request
from django.contrib.auth import get_user_model
User = get_user_model()
from django.test import Client
from Teams.models import Teams, Tasks, TaskUserMembership, TeamUserMembership, Comments

# # Create your tests here.

class FormTest(TestCase):
    def setUp(self):
        self.U1           = User.objects.create_user(username='hritik1', email='hritik1kumar.rd@gmail.com', password='password')
        self.U2           = User.objects.create_user(username='hritik2', email='hritik2kumar.rd@gmail.com', password='password')
        self.U3           = User.objects.create_user(username='hritik3', email='hritik3kumar.rd@gmail.com', password='password')
        self.U4           = User.objects.create_user(username='hritik4', email='hritik4kumar.rd@gmail.com', password='password')
        self.U5           = User.objects.create_user(username='hritik5', email='hritik5kumar.rd@gmail.com', password='password')
        self.U6           = User.objects.create_user(username='hritik6', email='hritik6kumar.rd@gmail.com', password='password')
        self.TM1          = Teams.objects.create(title='Team1', description='Team1 Description', teamAdmin=self.U1)
        
        self.M_User_Team1 = TeamUserMembership(teamMember=self.U2, teamName=self.TM1)
        self.M_User_Team1.save()
        self.M_User_Team2 = TeamUserMembership(teamMember=self.U3, teamName=self.TM1)
        self.M_User_Team2.save()
        
        self.TSK1         = Tasks.objects.create(title='Task1', description='Task1 Description', status='Planning', creator=self.U1, teams=self.TM1)
        
        self.M_User_Task1 = TaskUserMembership(taskMember=self.U2, taskName=self.TSK1)
        self.M_User_Task1.save()
        self.M_User_Task2 = TaskUserMembership(taskMember=self.U3, taskName=self.TSK1)
        self.M_User_Task2.save()

        self.COMNT1 = Comments.objects.create(comments='Comment bu task member 2', author=self.U2 , task=self.TSK1) 
        self.COMNT2 = Comments.objects.create(comments='Comment bu task member 3', author=self.U3 , task=self.TSK1)
        
        self.client = Client()
        self.client.login(username='hritik1', password='password')
        pass



    def test_login_form(self):
        # test Invalid data
        invalid_data = {
            "username": '',
            "password": "secret",
        }
        form = CustomLoginForm(request=request, data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        # test valid data
        valid_data = {
            "username": "user@test.com",
            "password": "secret",
        }
        form = CustomLoginForm(request=request, data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
        pass


    def test_signup_form(self):
        # test Invalid data
        invalid_data = {
            'email':'hindustan@gmalcom',
            'username' : "usercom",
            'password1': "secret",
            'password2': "not secret"
        }
        form = CustomSignupForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        # test valid data
        valid_data = {
            'email' : 'helloEmail@gmail.com',
            'username' : 'hello',
            'password1' : 'secret',
            'password2' : 'secret'
        }
        form = CustomSignupForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
        pass


""" Task and Team creation form is already implemented in test_views """


