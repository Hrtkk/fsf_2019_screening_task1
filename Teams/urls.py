from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Teams'
urlpatterns = [
    path('', views.IndexView.as_view(),name='teamsView'),
    path('createTeam/$', views.CreateTeams.as_view(), name='CreateTeam'),
    path('teamList/', views.TeamListView.as_view(), name='TeamList'),
    path('teamDetail/', views.TeamDetailView.as_view(), name='TeamDetail'),
    path(r'<int:teamId>/task/', views.TaskDetailView.as_view(), name='TaskDetail'),
    path(r'<int:team_id>/task/createTask/', views.CreateTask.as_view(), name='CreateTask'),
    path('task/taskDetail/', views.TaskDetailView.as_view(), name='TaskDetail'),
    path(r'<int:team_id>/task/<int:task_id>/update', views.UpdateTask.as_view(), name='UpdateTask'),
    path(r'<int:team_id>/task/(?P<pk>[\w]+)/delete', views.DeleteTask.as_view(), name='DeleteTask'),
    path(r'<int:team_id>/task/<int:task_id>/comment', views.CommentTask.as_view(), name='CommentTask'),
    
]

