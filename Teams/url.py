from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.Teams, name='teams'),
    url('tasksID/',include('Tasks.url')),
   
]