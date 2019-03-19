from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateResponseMixin, ContextMixin,View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from .forms import CustomTeamCreationForm
from .models import TeamList
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(View):
    # model = TeamList
    template_name = 'Teams/teams.html'
    # var1 = 0
    # var2 = 1
    
    def get(self, request, *args, **kwargs):
        # context = locals()
        # print(request.session)
        # print(request.session['_auth_user_id'],request.session['_auth_user_backend'],request.session['_auth_user_hash'])   # _auth_user_id, _auth_user_backend, _auth_user_hash
        print("TeamsIndex")
        # context['var1'] = self.var1
        # context['var2'] = self.var2
        return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     context = locals()
    #     print(request.POST)

    #     context['var1'] = self.var1
    #     context['var2'] = self.var2
    #     return render_to_response(self.template_name, context)


class CreateTeam(PassRequestMixin, SuccessMessageMixin,
                     CreateView):
    form_class = CustomTeamCreationForm
    template_name = 'Teams/teamCreatePop.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('Teams:teamsView')

class TeamDetails():
    template_name = 'Tasks/TaskDetailView.html'