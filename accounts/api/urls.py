from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
UserDetailAPIView,
    # AccountQuestionsAPIView,
)

urlpatterns = [

    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^(?P<username>[\w-]+)/$', UserDetailAPIView.as_view(), name='detail'),

    # url(r'^(?P<username>[\w-]+)/questions/$', AccountQuestionsAPIView.as_view(), name='questions'),

]