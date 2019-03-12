from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.TasksView, name='taskview'),
 
]