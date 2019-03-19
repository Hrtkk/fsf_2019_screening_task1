from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, TemplateView,View
from .forms import CustomTeamCreationForm, CustomTaskCreateForm
from django.shortcuts import redirect
from .models import Teams, TeamUserMembership
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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
    pass
    

class CreateTeams(CreateView):
    template_name = 'Teams/teamCreatePop.html'
    form_class = CustomTeamCreationForm
    success_url = '/teams/index'
    default_next = '/userAuth/profile'

    def get(self, request, *args, **kwargs):
        print("Hello")
        return render(request, self.template_name, {'form':self.form_class})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CustomTeamCreationForm(request.POST)
        print("Hey i am checking form")
        if form.is_valid():
            print("Form is valid")
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
    template_name = 'Task/TaskCreation.html'
    form_class = CustomTaskCreateForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = CustomTaskCreateForm(request.POST)
        if form.is_valid():
        #     title = form.cleaned_data['title']
        #     description = form.cleaned_data['description']
        #     status = form.cleaned_data['status']
        #     task = Tasks(title=title,description=description,status=status)
        #     task.save()
            return redirect('/home/')
        return redirect('/task/')


class TaskDetailView(DetailView):
    template_name = 'Task/TaskDetail.html'




