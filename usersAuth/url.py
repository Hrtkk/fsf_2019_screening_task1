from django.urls import path
from .views import CustomLoginView, CustomSignupView, ProfileView, IndexView

app_name = 'usersAuth'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', IndexView.as_view(), name='index'),
]
