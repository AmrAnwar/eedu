from django.conf.urls import url

from .views import (
    group_list,
profiles,
)

urlpatterns = [

    url(r'^groups/$', group_list, name='groups'),
    url(r'^groups/(?P<id>\d+)/users/$', profiles, name='profiles'),
]
