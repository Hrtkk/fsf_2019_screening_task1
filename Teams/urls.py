from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

app_name = 'Teams'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(),name='teamsView'),
    re_path(r'^createTeam/$', views.CreateTeams.as_view(), name='CreateTeam'),
    re_path(r'^(?P<team_id>[\w]+)/task/createTask/$', views.CreateTask.as_view(), name='CreateTask'),
    re_path(r'^(?P<team_id>[\w]+)/task/(?P<pk>[\w]+)/taskDetail/$', views.Task_DetailView, name='TaskDetail'),
    re_path(r'^(?P<team_id>[\w]+)/task/(?P<pk>[\w]+)/update/$', views.UpdateTask.as_view(), name='UpdateTask'),
    re_path(r'^(?P<team_id>[\w]+)/task/(?P<pk>[\w]+)/delete/$', views.DeleteTask.as_view(), name='DeleteTask'),
    re_path(r'^(?P<team_id>[\w]+)/task/(?P<task_id>[\w]+)/comment/$', views.CommentTask.as_view(), name='CommentTask'),
    # re_path(r'^(?P<team_id>[\w]+)/task/$', views.TaskDetailView.as_view(), name='TaskDetail'),
    re_path(r'^(?P<pk>[\w]+)/deleteTeam/$', views.deleteTeam.as_view(), name='deleteMember'),
    re_path(r'^(?P<team_id>[\w]+)/LeaveTeam/$', views.LeaveTeam.as_view(), name='LeaveTeam'),
]
