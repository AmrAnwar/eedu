from django.db.models import Q
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework import viewsets

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from news.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import HttpResponse, HttpResponseRedirect, Http404
from rest_framework.response import Response

from study.models import Unit,Part,Word, WordBank

from .permissions import IsOwnerOrReadOnly
from .serializers import (
    UnitListV1Serializer,
    UnitListSerializer,
    WordDetailSerializer,
    PartDetailFullSerializer,
    PartDetailSerializer,
    PartDetailWordSerializer,
    PartDetailTestSerializer,
WordBankDetailSerializer,
)
from django.contrib.auth.models import User


class PartDetailWordsAPIView(RetrieveAPIView):
    queryset = Part.objects.all()
    serializer_class = PartDetailWordSerializer
    lookup_field = 'id'


class PartDetailTestsAPIView(RetrieveAPIView):
    queryset = Part.objects.all()
    serializer_class = PartDetailTestSerializer
    lookup_field = 'id'


class UnitListAPIViewV2(ListAPIView):
    serializer_class = UnitListSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = PostPageNumberPagination
    def get_queryset(self):
        querset_list = Unit.objects.filter(wait=False)
        return querset_list


class UnitListAPIViewV1(ListAPIView):
    serializer_class = UnitListV1Serializer
    pagination_class = PostPageNumberPagination
    def get_queryset(self):
        querset_list = Unit.objects.filter(wait=False)
        return querset_list


class PartListAPIView(ListAPIView):
    serializer_class = PartDetailFullSerializer
    pagination_class = PostPageNumberPagination
    def get_queryset(self):
        querset_list = Part.objects.filter(wait=False)
        q = self.request.GET.get("q")
        if q:
            querset_list = Part.objects.filter(id=int(q))
        return querset_list


class WordListAPIView(APIView):
    def get_object(self, id):
        try:
            return Part.objects.get(id=id)
        except Part.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        part = Part.objects.get(id=id)
        queryset = Word.objects.filter(part=part)
        serializer = WordDetailSerializer(queryset)
        return Response(serializer.data)


class WordStarToggle(APIView):
    def get(self, request, word_id=None, user_id=None, format=None):
        word = get_object_or_404(Word, id=word_id)
        user = get_object_or_404(User, id=user_id)
        toggle = False
        if user in word.users.all():
            word.users.remove(user)
        else:
            word.users.add(user)
            toggle = True
        word.save()
        data = {
            "toggle": toggle,
        }
        return Response(data)


# class UserPartDetailWordsAPIView(ListAPIView):
#     serializer_class = WordDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         self.user = get_object_or_404(User, id=kwargs.get('user_id'))
#         self.part = get_object_or_404(Part, id=kwargs.get('part_id'))
#         return super(UserPartDetailWordsAPIView, self).get(self, request)
#
#     def get_queryset(self):
#         queryset = self.user.words.filter(part=self.part)
#         serializer = WordDetailSerializer(queryset, many=True)
#         print serializer
#         return Response(serializer.data)

class UserPartDetailWordsAPIView(APIView):
    def get(self, request, part_id=None, user_id=None, format=None):
        user = get_object_or_404(User, id=user_id)
        part = get_object_or_404(Part, id=part_id)
        queryset = user.words.filter(part=part)
        serializer = WordDetailSerializer(queryset, many=True)
        print serializer
        return Response(serializer.data)


class WordBankView(viewsets.ModelViewSet):
    serializer_class = WordBankDetailSerializer
    # queryset = WordBank.objects.all()
    filter_backends = [SearchFilter]

    def get_queryset(self):
        if self.request.GET.get("user"):
            user_id = self.request.GET.get("user")
            user = get_object_or_404(User, id=user_id)
            qs = WordBank.objects.filter(user=user)
            return qs