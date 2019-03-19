from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, TemplateView,View
from .forms import CustomTeamCreationForm
# Create your views here.
from .forms import CustomTeamCreationForm
from django.shortcuts import redirect
from .models import Teams

class CreateTeams(View):
    template_name = 'Teams/teamCreatePop.html'
    form_class = CustomTeamCreationForm
    success_url = '/teams/index'
    default_next = '/userAuth/profile'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = CustomTeamCreationForm(request.POST)
        print("Hey i am checking form")
        if form.is_valid():
            print("Yes form is valid")
            # form.save()
            obj = Teams()
            print(form.cleaned_data)
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['description']
            # obj.teamMember = form.cleaned_data[]
            obj.save()
        return redirect('/teams/')


class TeamListView(ListView):
    template_name = 'teamList.html'

    def get(self, request, *args, **kwargs):
        pass


class TeamDetailView(DetailView):
    template_name = 'teamDetail.html'

    def get(self, request, *args, **kwargs):
        pass


class IndexView(TemplateView):
    template_name = 'Teams/teams.html'



