from django.conf.urls import url
from django.contrib import admin

from .views import (
    UnitListAPIView,
    UnitDetailAPIView,
WordListAPIView,
PartListAPIView,
PartDetailWordsAPIView,
PartDetailTestsAPIView,
    # TestListAPIView,
)

urlpatterns = [

    url(r'^units/$', UnitListAPIView.as_view(), name='list'),
    url(r'^parts/$', PartListAPIView.as_view(), name='list-parts'),
    url(r'^parts/words/(?P<id>[\d-]+)/$', PartDetailWordsAPIView.as_view(), name='part-words'),
    url(r'^parts/tests/(?P<id>[\d-]+)/$', PartDetailTestsAPIView.as_view(), name='part-tests'),

    url(r'^units/(?P<slug>[\w-]+)/$', UnitDetailAPIView.as_view(), name='unit-detail'),
    url(r'^parts/(?P<slug>[\w-]+)/$', WordListAPIView.as_view(), name='part-detail'),
    # url(r'parts/(?P<slug>[\w-]+)/tests/$',TestListAPIView.as_view(),name='part-test'),

]