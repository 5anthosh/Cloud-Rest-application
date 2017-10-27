from Api.views import field_list, field_get, history_list
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r"^$", field_list),
    url(r"^(?P<field>[a-zA-Z0-9]+)/$", field_get),
    url(r"^(?P<field>[a-zA-Z0-9]+)/history/$", history_list)
]
urlpatterns = format_suffix_patterns(urlpatterns)
