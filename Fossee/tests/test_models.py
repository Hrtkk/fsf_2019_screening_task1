from django.test import SimpleTestCase, TestCase, RequestFactory
from django.contrib.auth import get_user_model
from Teams.models import Teams, Tasks, TaskUserMembership, TeamUserMembership, Comments
User = get_user_model()

# Here you define the test functions

class modelTest(TestCase):
    def setUp(self):
        self.U1           = User.objects.create_user(username='hritik1', email='hritik1kumar.rd@gmail.com', password='password')
        self.U2           = User.objects.create_user(username='hritik2', email='hritik2kumar.rd@gmail.com', password='password')
        self.U3           = User.objects.create_user(username='hritik3', email='hritik3kumar.rd@gmail.com', password='password')
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
        pass

    def test_accounts(self):
        self.assertEqual(self.U1.username, 'hritik1')
        self.assertEqual(self.U2.username, 'hritik2')
        self.assertEqual(self.U3.username, 'hritik3')
        self.assertEqual(self.U1.email, 'hritik1kumar.rd@gmail.com')
        self.assertEqual(self.U2.email, 'hritik2kumar.rd@gmail.com')
        self.assertEqual(self.U3.email, 'hritik3kumar.rd@gmail.com')
        pass

    def test_Team_model(self):
        self.assertEqual(self.TM1.title, 'Team1')
        self.assertEqual(self.TM1.description, 'Team1 Description')
        self.assertEqual(self.TM1.teamAdmin, self.U1)
        self.assertNotEqual(self.TM1.teamAdmin, self.U2)
        self.assertEqual(self.TM1, self.U2.MemberTeams.all()[0])
        self.assertEqual(self.TM1, self.U3.MemberTeams.all()[0])
        pass

    def test_Task_model(self):
        self.assertEqual(self.TSK1.title, 'Task1')
        self.assertEqual(self.TSK1.description, 'Task1 Description')
        self.assertEqual(self.TSK1.status, 'Planning')
        self.assertEqual(self.TSK1.creator, self.U1)
        self.assertEqual(self.TSK1.teams, self.TM1)
        self.assertEqual(self.TSK1, self.U2.TasksMember.all()[0])
        self.assertEqual(self.TSK1, self.U3.TasksMember.all()[0])
        pass

    def test_comments_model(self):
        self.assertEqual(self.TSK1.comments.all()[0].comments, 'Comment bu task member 2')
        self.assertEqual(self.TSK1.comments.all()[1].comments, 'Comment bu task member 3')
        self.assertEqual(self.COMNT1.author, self.U2)
        self.assertEqual(self.COMNT2.author, self.U3)
        pass

 