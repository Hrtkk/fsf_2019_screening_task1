from django.urls import path
from .views import CustomLoginView, CustomSignupView, ProfileView, IndexView, LogoutView

app_name = 'usersAuth'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', IndexView.as_view(), name='index'),
]
