from django.conf.urls import url

from .views import (
    UnitListAPIViewV1,
    UnitListAPIViewV2,
    # UnitDetailAPIView,
    WordListAPIView,
    PartListAPIView,
    PartDetailWordsAPIView,
    PartDetailTestsAPIView,
    WordStarToggle,
    UserPartDetailWordsAPIView,
    WordBankView,
    ExerciseView,
    ExamView,
McqTestViw,

    # TestListAPIView,
)

# router = DefaultRouter()
# router.register(r'bank', WordBankView, base_name='bank')

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^mcq/$', McqTestViw.as_view(), name='mcq'),
    url(r'^exam/$', ExamView.as_view({'get': 'list',
                                             })),
    url(r'^exercise/$', ExerciseView.as_view({'get': 'list',
                                              })),
    url(r'^bank/$', WordBankView.as_view({'get': 'list',
                                          'post': 'create'})),

    url(r'^bank/(?P<pk>\d+)/$', WordBankView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'patch': 'update'})),

    url(r'^units/$', UnitListAPIViewV1.as_view(), name='list-v1'),
    url(r'^units/v2/$', UnitListAPIViewV2.as_view(), name='list-v2'),
    url(r'^parts/$', PartListAPIView.as_view(), name='list-parts'),
    url(r'^parts/words/(?P<id>[\d-]+)/$', PartDetailWordsAPIView.as_view(), name='part-words'),
    url(r'^parts/words/(?P<part_id>[\d-]+)/(?P<user_id>[\d-]+)$', UserPartDetailWordsAPIView.as_view(),
        name='user-part-words'),

    url(r'^parts/tests/(?P<id>[\d-]+)/$', PartDetailTestsAPIView.as_view(), name='part-tests'),
    url(r'^wordtoggle/(?P<word_id>[\d-]+)/(?P<user_id>[\d-]+)/', WordStarToggle.as_view(),
        name="word-toggle"),
    # url(r'^units/(?P<slug>[\w-]+)/$', UnitDetailAPIView.as_view(), name='unit-detail'),
    url(r'^parts/(?P<id>[\w-]+)/$', WordListAPIView.as_view(), name='part-detail'),
    # url(r'parts/(?P<slug>[\w-]+)/tests/$',TestListAPIView.as_view(),name='part-test'),

]
