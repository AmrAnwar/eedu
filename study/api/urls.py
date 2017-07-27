from django.conf.urls import url
from django.contrib import admin

from .views import (
    UnitListAPIView,
    UnitDetailAPIView,
WordListAPIView,
# TestListAPIView,
)

urlpatterns = [

    url(r'^units/$', UnitListAPIView.as_view(), name='list'),
    url(r'^units/(?P<slug>[\w-]+)/$', UnitDetailAPIView.as_view(), name='unit-detail'),
    url(r'^parts/(?P<slug>[\w-]+)/$', WordListAPIView.as_view(), name='part-detail'),
    # url(r'parts/(?P<slug>[\w-]+)/tests/$',TestListAPIView.as_view(),name='part-test'),

]