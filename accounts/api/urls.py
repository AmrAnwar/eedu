from django.conf.urls import url

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    UserProfileModelViewSet,
    UserLogoutAPIView,
    UserLoginTestAPIView,
)

urlpatterns = [

    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^login/test/$', UserLoginTestAPIView.as_view(), name='login'),

    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^(?P<username>[\w-]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/logout/$', UserLogoutAPIView.as_view(), name='logout'),
    url(r'^(?P<username>[\w-]+)/profile$', UserProfileModelViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'put': 'update',
        'delete': 'destroy',
    }), name='profile-detail'),
    # url(r'^(?P<username>[\w-]+)/questions/$', AccountQuestionsAPIView.as_view(), name='questions'),
]