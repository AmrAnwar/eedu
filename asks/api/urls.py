from django.conf.urls import url

from .views import (
    AskListAPIView,
    AskDetailAPIView,
    AskDeleteAPIView,
    AskUpdateAPIView,
   AskCreateAPIView,
AccountQuestionsAPIView,

)

urlpatterns = [
    url(r'^create/$', AskCreateAPIView.as_view(), name='create'),
    url(r'^(?P<username>[\w-]+)/$', AccountQuestionsAPIView.as_view(), name='questions'),
    url(r'^$', AskListAPIView.as_view(), name='list'),
    url(r'^(?P<id>[\d-]+)/$', AskDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\d-]+)/edit$', AskUpdateAPIView.as_view(), name='edit'),
    url(r'^(?P<id>[\d-]+)/delete$', AskDeleteAPIView.as_view(), name='delete'),

]