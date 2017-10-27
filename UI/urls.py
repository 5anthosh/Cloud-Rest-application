from django.conf.urls import url
from .views import user_create, login_user, home, logout_user
urlpatterns = [
    url(r'^$', home),
    url(r'^create/$', user_create),
    url(r'^login/$', login_user),
    url(r'^logout/$', logout_user),
]