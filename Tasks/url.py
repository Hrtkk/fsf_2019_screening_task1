from django.urls.conf import path
from .views import CreateTask, TaskDetailView

app_name = 'Task'
urlpatterns = [
    path('createTask', CreateTask.as_view(), name='CreateTask'),
    path('TaskDetail', TaskDetailView.as_view(), name='TaskDetail'),
]
