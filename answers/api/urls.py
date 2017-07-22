from django.conf.urls import url
from django.contrib import admin

from .views import (
    AnswerListAPIView,
    AnswerDetailAPIView,
    AnswerDeleteAPIView,
    AnswerUpdateAPIView,
    AnswerCreateAPIView,
)

urlpatterns = [
    url(r'^$', AnswerListAPIView.as_view(), name='list'),
    url(r'^create/$', AnswerCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/', AnswerDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', AnswerUpdateAPIView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete$', AnswerDeleteAPIView.as_view(), name='delete'),
]