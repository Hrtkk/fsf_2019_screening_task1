from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, TemplateView,View, UpdateView, DeleteView
from .forms import CustomTeamCreationForm, CustomTaskCreateForm, CommentsForm
from django.shortcuts import redirect, get_object_or_404
from .models import Teams, TeamUserMembership, Tasks, TaskUserMembership, Comments
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.http import Http404
# from .models import Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
User = get_user_model()


def formTeam(request, form):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    teamAdmin = User.objects.filter(email=request.user)[0]
    T = Teams(title=title,description=description,teamAdmin=teamAdmin)
    T.save()
    for M in form.cleaned_data['members']:
        teamMember = User.objects.filter(email=M)[0]
        print('hello')
        print(teamMember.username)
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
    
    
class CreateTeams(LoginRequiredMixin, CreateView):
    template_name = 'Teams/teamCreatePop.html'
    form_class = CustomTeamCreationForm
    success_url = '/teams/index'
    
    login_url = '/home/'
    # redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        kw = super(CreateTeams, self).get_form_kwargs()
        kw['request'] = self.request 
        return kw

    def get(self, request, *args, **kwargs):
        form_class = CustomTeamCreationForm(request.GET, request=request)
        return render(request, self.template_name, {'form':form_class,'user':request.user})

    def post(self, request, *args, **kwargs):
        form = CustomTeamCreationForm(request.POST, request=request)
        if form.is_valid():
            formTeam(request, form)
        return redirect('/teams/')


class TeamListView(LoginRequiredMixin, ListView):
    template_name = 'Teams/teamList.html'
    login_url = '/home/'
    def get(self, request, *args, **kwargs):
        pass


class TeamDetailView(LoginRequiredMixin, DetailView):
    template_name = 'teamDetail.html'
    login_url = '/home/'
    def get(self, request, *args, **kwargs):
        pass


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'Teams/TeamIndex.html'
    login_url = '/home/'
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        if request.user.is_authenticated:
            teamAdmin = User.objects.filter(email=request.user)[0]
            context['MemberTeams'] = teamAdmin.MemberTeams.all()
            context['AdminTeams'] = teamAdmin.AdminTeams.all()
            context['user'] = request.user
        return render_to_response(self.template_name,context)


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'Teams/taskCreatePop.html'
    form_class = CustomTaskCreateForm
    success_url = '/teams/'
    login_url = '/home/'

    def get(self, request, team_id, *args, **kwargs):
        context = {}
        team = Teams.objects.filter(pk=team_id)[0]
        form_class = CustomTaskCreateForm(request.GET, request=request, team=team)
        context['team'] = team
        context['form'] = form_class
        print(team)
        return render(request, self.template_name, context)

    def post(self, request, team_id, *args, **kwargs):
        form = CustomTaskCreateForm(request.POST, request=request)
        print("Checking form validity")
        if form.is_valid():
            formTask(request, form, team_id)
            return  redirect('/teams/{}/task/'.format(team_id))
        return redirect('/')


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'Teams/TaskDetail.html'
    login_url = '/home/'
    def get(self, request, teamId=0, *args, **kwargs):
        context = {}
        team = Teams.objects.filter(pk=teamId)[0]
        task = team.Tasks.all()
        member = team.teamMember.all()
        if request.user.is_authenticated:
            teamAdmin = User.objects.filter(email=request.user)[0]
            context['MemberTeams'] = teamAdmin.MemberTeams.all()
            context['AdminTeams']= teamAdmin.AdminTeams.all()
            context['user'] = request.user
        context['tasks'] = task
        context['team'] = team
        context['member'] = member
        print(task)
        return render(request, self.template_name, context)


class CommentTask(LoginRequiredMixin, CreateView):
    template_name = 'Teams/comment.html'
    form_class = CommentsForm
    success_url = '/teams'
    login_url = '/home/'

    def get(self, request, teamId=0, task_id=0, *args, **kwargs):
        context = {}
        context['form'] = self.form_class
        com = Tasks.objects.filter(id=task_id)[0]
        context['comments'] = com.comments.all()
        print(com.comments.all())
        return render(request, self.template_name, context)


    def post(self, request, teamId=0, task_id=0, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comments']
            t = Tasks.objects.get(pk=task_id)
            Com = Comments(task=t, comments=comment, author = request.user)
            Com.save()
            print(task_id)
            print('comments saved')
            return redirect('/teams')
        return redirect('/')

    

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Tasks
    login_url = '/home/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteTask, self).get_object()
        if not obj.creator == self.request.user:
            raise Http404
        return obj
    
    def get_success_url(self):
        return reverse('Teams:teamsView')
    


class UpdateTask(LoginRequiredMixin, UpdateView):
    login_url = '/home/'
    model = Tasks
    fields = ['status']
    template_name_suffix = '_update_form'
    success_url = '/teams'
    

