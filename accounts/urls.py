from django.conf.urls import url

from .views import (
    group_list,
profiles,
)

urlpatterns = [

    url(r'^groups/efvegewg32e423/$', group_list, name='groups'),
    url(r'^groups/efvegewg32e423/(?P<id>\d+)/users/$', profiles, name='profiles'),
]
