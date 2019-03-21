from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, TemplateView,View
from .forms import CustomTeamCreationForm, CustomTaskCreateForm
from django.shortcuts import redirect, get_object_or_404
from .models import Teams, TeamUserMembership, Tasks, TaskUserMembership
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
# from .models import Tasks
User = get_user_model()


def formTeam(request, form):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    teamAdmin = User.objects.filter(email=request.user)[0]
    T = Teams(title=title,description=description,teamAdmin=teamAdmin)
    T.save()
    for M in form.cleaned_data['members']:
        teamMember = User.objects.filter(email=M)[0]
        m1 = TeamUserMembership(teamName=T, teamMember= teamMember)
        m1.save()



def formTask(request, form, team_id):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    status = form.cleaned_data['status']
    taskAdmin = User.objects.filter(email=request.user)[0]
    team = Teams.objects.get(pk=team_id)
    T = Tasks(title=title,description=description,status=status,teams=team,creator=taskAdmin)
    
    T.save()
    
    
    

class CreateTeams(CreateView):
    template_name = 'Teams/teamCreatePop.html'
    form_class = CustomTeamCreationForm
    success_url = '/teams/index'
    default_next = '/userAuth/profile'
    # model = Teams
    # fields = '__all__'
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {'form':self.form_class})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CustomTeamCreationForm(request.POST)
        if form.is_valid():
            formTeam(request, form)
        return redirect('/teams/')


class TeamListView(ListView):
    template_name = 'Teams/teamList.html'
    def get(self, request, *args, **kwargs):
        pass


class TeamDetailView(DetailView):
    template_name = 'teamDetail.html'

    def get(self, request, *args, **kwargs):
        pass


class IndexView(TemplateView):
    template_name = 'Teams/teams.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        # print(request.user.keys())
        if request.user.is_authenticated:
            teamAdmin = User.objects.filter(email=request.user)[0]
            context['AdminTeams'] = teamAdmin.MemberTeams.all()
            context['MemberTeams'] = teamAdmin.AdminTeams.all()
            context['user'] = request.user
        return render_to_response(self.template_name,context)


class CreateTask(CreateView):
    template_name = 'Teams/taskCreatePop.html'
    form_class = CustomTaskCreateForm
    success_url = '/teams/'
    default_next = '/'

    def get(self, request, team_id, *args, **kwargs):
        context = {}
        team = Teams.objects.filter(pk=team_id)[0]
        context['team'] = team
        context['form'] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, team_id, *args, **kwargs):
        form = CustomTaskCreateForm(request.POST)
        # print()
        print("Checking form validity")
        if form.is_valid():
            formTask(request, form, team_id)
            return redirect('/teams/{}/task/'.format(team_id))
        return redirect('/')


class TaskDetailView(DetailView):
    template_name = 'Teams/TaskDetail.html'
    def get(self, request, teamId=0, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            teamAdmin = User.objects.filter(email=request.user)[0]
            context['MemberTeams'] = teamAdmin.MemberTeams.all()
            context['AdminTeams']= teamAdmin.AdminTeams.all()
            context['user'] = request.user
        team = Teams.objects.filter(pk=teamId)[0]
        task = team.Tasks.all()
        member = team.teamMember.all()
        print(member)
    
        context['tasks'] = task
        context['team'] = team
        context['member'] = member
        return render(request, self.template_name,context)




