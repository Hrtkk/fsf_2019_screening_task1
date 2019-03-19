from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Teams'
urlpatterns = [
    path('', views.IndexView.as_view(),name='teamsView'),
    path('createTeam', views.CreateTeams.as_view(), name='createTeam'),
    path('teamList', views.TeamListView.as_view(), name='TeamList'),
    path('teamDetail', views.TeamDetailView.as_view(), name='TeamDetail'),
    # path('tasks/', include('Tasks.urls', namespace='Task')),
   

]

