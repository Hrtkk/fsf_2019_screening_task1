from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views
from . import settings
from django.views.generic import RedirectView

app_name='Fossee'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/teams/'),name='index'),
    path('teams/tasksID/',include('Tasks.url',namespace='tasks')),
    path('teams/',include('Teams.url',namespace='team')),
    path('usersAuth/',include('usersAuth.url')),
    url('admin/', admin.site.urls),
    path('usersAuth/', include('django.contrib.auth.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
