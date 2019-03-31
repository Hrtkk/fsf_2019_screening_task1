from django.test import TestCase, Client
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import reverse
from django.contrib.auth.models import AnonymousUser
from Teams.models import Teams, Tasks, TeamUserMembership, TaskUserMembership, Comments
from datetime import datetime
class modelTestForViews(TestCase):
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

    def test_home_view(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        pass


    def test_teams_view(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('Teams:teamsView'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/TeamIndex.html')  
        pass


    def test_task_view(self):
        response = self.client.get('/teams/')
        self.assertEqual(str(response.context['user']), 'hritik1kumar.rd@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/TeamIndex.html')
        pass


    def test_login_view(self):
        response = self.client.get('/accounts/login/')
        response1 = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTemplateUsed(response1, 'registration/login.html')
        data = {
            'username':'hritik1',
            'password': 'password'
        }
        response1 = self.client.post(reverse('account:login'), data=data, follow=True)
        self.assertEqual(response1.context['user'].email,'hritik1kumar.rd@gmail.com')
        pass


    def test_logout_view(self):
        response1 = self.client.get(reverse('account:login'))
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'registration/login.html')
        data = {
            'username':'hritik1',
            'password': 'password'
        }
        response1 = self.client.post(reverse('account:login'), data=data, follow=True)
        self.assertTrue(response1.context['user'].is_authenticated)
        self.assertEqual(response1.context['user'].email,'hritik1kumar.rd@gmail.com')
        response1 = self.client.post(reverse('account:logout'), follow=True)
        self.assertRedirects(response1, 'home/')
        self.assertEqual(response1.status_code, 200)
        self.assertFalse(response1.context['user'].is_authenticated)
        pass
    
    
    def test_team_create_view(self):
        response = self.client.get('/teams/createTeam/')
        response1 = self.client.get(reverse('Teams:CreateTeam'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/teamCreatePop.html')
        self.assertTemplateUsed(response1, 'Teams/teamCreatePop.html')
        data = {
            'title' : 'New Nita Team',
            'description' : 'This is new NIT Agartala Team which is doing django project',
            'date' : '12/02/2019',
            'members':[str(self.U3.id), str(self.U5.id), str(self.U6.id)]
        }
        response1 = self.client.post(reverse('Teams:CreateTeam'),data=data, follow=True)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(Teams.objects.all()[1].title, 'New Nita Team')
        pass
    
    
    def test_task_create_view(self):
        response = self.client.get('/teams/{}/task/createTask'.format(Teams.objects.all()[0].id), follow=True)
        response1 = self.client.get(reverse('Teams:CreateTask', kwargs={'team_id':Teams.objects.all()[0].id}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/taskCreatePop.html')
        self.assertTemplateUsed(response1, 'Teams/taskCreatePop.html')
        data = {
            'title' : 'New Programming Task',
            'description' : 'This task is a very important task which ',
            'status' : 'Done',
            'Assigned' : str(self.U2.id)
        }
        response1 = self.client.post(reverse('Teams:CreateTask', kwargs={'team_id':Teams.objects.all()[0].id}),
                        data=data, follow=False)
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(Tasks.objects.all()[1].title,'New Programming Task' )
        pass
    
    
    def test_comment_post_view(self):
        """ 
            This test case is for checking of proper implementation of views for comments.
            At the very early stage availability of task is ensured. After that a get request is sent to the url 'Teams:CommentTask'
            to ensure that it is responding with corrwct template file via both hard coded and reverse url resolution method.
            after ensuring everything is working properly. 
            A post request is sent with dummy comment on given task of particular team which comments and status code is matched against
            the expected value.

        """ 
        self.assertEqual(Tasks.objects.count(), 1)
        response = self.client.get('/teams/{}/task/{}/comment/'.format(Teams.objects.all()[0].id, Tasks.objects.all()[0].id))
        response1 = self.client.get(reverse('Teams:CommentTask', kwargs = {'team_id':Teams.objects.all()[0].id, 'task_id':Tasks.objects.all()[0].id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/comment.html')
        self.assertTemplateUsed(response1, 'Teams/comment.html')
        
        # dummy comment data
        data = {'comments':'This is very heavy task!!'}
        
        # post request 
        response1 = self.client.post(reverse('Teams:CommentTask', 
                    kwargs = {'team_id':Teams.objects.all()[0].id, 
                    'task_id':Tasks.objects.all()[0].id}),
                    data=data,
                    follow=True
                )
        self.assertEqual(response1.status_code, 200)
        self.assertRedirects(response1, '/teams/')

        # expected comments on the task
        # self.assertEqual(Comments.objects.get(pk=11).comments, 'This is very heavy task!!')
        pass


