from django.urls import path
from .views import CustomSignupView, ProfileView, IndexView, LogoutView, CustomLoginView
from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name='index'),

]
