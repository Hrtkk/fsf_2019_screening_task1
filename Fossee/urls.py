from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views
from . import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('usersAuth/',include('usersAuth.url')),
    path('usersAuth/', include('django.contrib.auth.urls')),
    url('Tasks/',include('Tasks.url')),
    url('Teams/',include('Teams.url')),
    url('admin/', admin.site.urls),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
