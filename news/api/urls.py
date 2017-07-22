from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView,
    PostWaitListAPIView
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/edit$', PostUpdateAPIView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete$', PostDeleteAPIView.as_view(), name='delete'),
    url(r'^wait/$', PostWaitListAPIView.as_view(), name='wait-list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),

]