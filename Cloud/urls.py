from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views

from Api.views import update

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/(?P<channel>[a-zA-Z0-9]+)/', include('Api.urls')),
    url(r'^update/$', update),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^user/', include('UI.urls')),
]
