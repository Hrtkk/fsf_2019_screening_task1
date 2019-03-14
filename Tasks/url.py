from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='Tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='taskview'),
    path(r'createTask/',views.CreateTask.as_view(),name="createTask")
]