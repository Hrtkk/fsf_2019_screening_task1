from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from django.shortcuts import reverse
User = get_user_model()
from account.admin import UserCreationForm
from Teams.forms import CustomTeamCreationForm
from Teams.models import Teams, Tasks


class Fossee_Url_test(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='hritik1', email='hritik1kumar.rd@gmail.com',password='password')
        team = Teams.objects.create(title="FOSSEETeam",teamAdmin = user1, description="This Team is the best team in this projects hub")
        task = Tasks.objects.create(title='FOSSEETask',creator=user1, description='Description',teams=team)
        self.taskId = Tasks.objects.get(title='FOSSEETask').id
        self.teamId = Teams.objects.get(title='FOSSEETeam').id

    def test_registration_get_url(self):
        response = self.client.get(reverse('account:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.failUnless(isinstance(response.context['form'], UserCreationForm)) 


    def test_registration_post_url(self):
        client = Client()
        response = client.post(reverse('account:signup'), 
                                        data={'username':'hrtkkumar',
                                            'email':'hritikkumar.rd@gmail.com',
                                            'password1':'password',
                                            'password2':'password'},
                                            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/home/', status_code = 302, target_status_code=200)
        self.assertEqual(User.objects.count(), 2)
        client.login(username='hrtkkumar',password='password')
        response = client.get('/teams/',follow=False)

        self.assertEqual(response.status_code, 200)
        pass

    def test_login_url(self):
        client = Client()
        response = client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        response = client.post(reverse('account:login'), 
                                    data={
                                        'username':'hritik1',
                                        'password':'password'
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/teams/')
        response = client.get('/teams/',follwo=True)
        self.assertTrue(response.context['user'].is_authenticated)
        pass


    def test_createTeam_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:CreateTeam'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/teamCreatePop.html')
        pass


    def test_createTask_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:CreateTask', kwargs={'team_id':self.teamId}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/taskCreatePop.html')
        

    def test_commentTask_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:CommentTask', kwargs={'team_id':self.teamId,
                                                        'task_id':int(self.taskId)}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/comment.html')
        
    
    def test_delete_Task_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:DeleteTask', kwargs={'team_id':self.teamId,
                                                        'pk':int(self.taskId)}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/tasks_confirm_delete.html')
        

    def test_Update_task_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:UpdateTask', kwargs={'team_id':self.teamId,
                                                        'pk':int(self.taskId)}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/tasks_update_form.html')
        

    def test_Delete_team_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:deleteMember', kwargs={'pk':self.teamId}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/teams_confirm_delete.html')
        

    def test_Leave_team_url(self):
        client = Client()
        client.login(username='hritik1', password='password')
        response = client.get(reverse('Teams:LeaveTeam', kwargs={'team_id':self.teamId}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Teams/LeaveTeam.html')
        

    # def test_Task_detail_url(self):
    #     client = Client()
    #     client.login(username='hritik1', password='password')
    #     response = client.get(reverse('Teams:TaskDetail', kwargs={'team_id':self.teamId,
    #                                                     'pk':self.taskId}), follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'Teams/TaskDetail.html')
        

   