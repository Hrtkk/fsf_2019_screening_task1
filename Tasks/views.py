from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateResponseMixin, ContextMixin,View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from .forms import CustomTaskCreationForm
from .models import TaskList
from bootstrap_modal_forms.mixins import PassRequestMixin
# Create your views here.

class TasksView(View):
    model = TaskList
    template_name = 'Tasks/TasksView.html'
    var1 = 0
    var2 = 1
    
    def get(self, request, *args, **kwargs):
        context = locals()
        context['var1'] = self.var1
        context['var2'] = self.var2
        return render_to_response(self.template_name, context)


class CreateTask(PassRequestMixin, SuccessMessageMixin,
                     CreateView):
    form_class = CustomTaskCreationForm
    template_name = 'Tasks/taskCreatePop.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('taskView')


class TaskDetails():
    template_name = 'Tasks/TaskDetailView.html'