from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'Teams'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='teamsView'),
    url(r'^createTeam/$',views.CreateTeam.as_view(),name='createTeam'),
]