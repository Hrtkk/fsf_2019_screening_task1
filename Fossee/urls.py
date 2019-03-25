from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from . import views
from . import settings
from django.views.generic import RedirectView

app_name='Fossee'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='home/'),name='index'),
    path('home/',views.index, name='home'),
    path('teams/',include('Teams.urls',namespace='Teams')),
    path('accounts/',include('account.urls',namespace='Accounts')),
    url('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
