from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Teams'
urlpatterns = [
    path('', views.IndexView.as_view(),name='teamsView'),
    path('createTeam/', views.CreateTeams.as_view(), name='CreateTeam'),
    path('teamList/', views.TeamListView.as_view(), name='TeamList'),
    path('teamDetail/', views.TeamDetailView.as_view(), name='TeamDetail'),
    path('<int:teamId>/task/', views.TaskDetailView.as_view(), name='TaskDetail'),
    path('<int:team_id>/task/createTask/', views.CreateTask.as_view(), name='CreateTask'),
    path('task/taskDetail/', views.TaskDetailView.as_view(), name='TaskDetail'),
    path('<int:team_id>/task/(?P<pk>[\w]+)/update/', views.UpdateTask.as_view(), name='UpdateTask'),
    path('<int:team_id>/task/(?P<pk>[\w]+)/delete/', views.DeleteTask.as_view(), name='DeleteTask'),
    path('<int:team_id>/task/<int:task_id>/comment/', views.CommentTask.as_view(), name='CommentTask'),
    
]

