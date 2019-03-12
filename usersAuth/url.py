# Django
from django.urls import path
# Project
from . import views


app_name = 'usersAuth'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
