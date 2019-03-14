from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views
from . import settings


app_name='Fossee'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$',include('Teams.url',namespace='teams')),
    
    path('usersAuth/',include('usersAuth.url')),
    path('usersAuth/', include('django.contrib.auth.urls')),
    url('teams/tasksID/',include('Tasks.url',namespace='tasks')),
    url('admin/', admin.site.urls),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
