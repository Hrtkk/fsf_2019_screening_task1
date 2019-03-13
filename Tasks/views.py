from django.shortcuts import render

# Create your views here.
def TasksView(response):
    return render(response,'Tasks/tasks.html')