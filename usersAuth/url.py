# Django
from django.urls import path
# Project
from . import views


app_name = 'usersAuth'
urlpatterns = [

    path('signup/', views.CustomSignupView.as_view(), name='signup'),
    path('', views.CustomLoginView.as_view(), name='LogIn'),
    # path(r'^$', views.IndexView.as_view(), name='profile'),
]
