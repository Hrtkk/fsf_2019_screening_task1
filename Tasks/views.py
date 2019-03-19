from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import CustomTaskCreateForm
from .models import Tasks


# Create your views here.
class CreateTask(CreateView):
    template_name = 'Task/TaskCreation.html'
    form_class = CustomTaskCreateForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = CustomTaskCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            task = Tasks(title=title,description=description,status=status)
            task.save()
            return redirect('/home/')
        return redirect('/task/')


class TaskDetailView(DetailView):
    template_name = 'Task/TaskDetail.html'
