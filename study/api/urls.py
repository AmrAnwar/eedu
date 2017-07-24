from django.conf.urls import url
from django.contrib import admin

from .views import (
    UnitListAPIView,
    UnitDetailAPIView,
WordListAPIView,
)

urlpatterns = [

    url(r'^units/$', UnitListAPIView.as_view(), name='list'),
    url(r'^units/(?P<slug>[\w-]+)/$', UnitDetailAPIView.as_view(), name='unit-detail'),
    url(r'^parts/(?P<slug>[\w-]+)/$', WordListAPIView.as_view(), name='part-detail'),

]