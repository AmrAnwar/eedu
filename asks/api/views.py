from django.db.models import Q
from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,


)
from django.http import HttpResponse, HttpResponseRedirect, Http404

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from news.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
from asks.models import Ask
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    AskDetailSerializer,
    AskListSerializer,
    AskCreateUpdateSerializer,
    UserQuestionsSerializer,
)
from django.contrib.auth import get_user_model
User = get_user_model()


# class AccountQuestionsAPIView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserQuestionsSerializer
#     lookup_field = 'username'

class AccountQuestionsAPIView(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username=None, format=None):
        user = User.objects.get(username=username)
        queryset = Ask.objects.filter(user=user).filter(~Q(replay=None))
        serializer = UserQuestionsSerializer(queryset, many=True)
        return Response(serializer.data)


class AskCreateAPIView(CreateAPIView):
    queryset = Ask.objects.all()
    serializer_class = AskCreateUpdateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

#
class AskDetailAPIView(RetrieveAPIView):
    queryset = Ask.objects.all()
    serializer_class = AskDetailSerializer
    lookup_field = 'id'


#
class AskUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ask.objects.all()
    serializer_class = AskCreateUpdateSerializer
    lookup_field = 'id'
    # permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()
        #email send_email

class AskDeleteAPIView(DestroyAPIView):
    queryset = Ask.objects.all()
    serializer_class = AskDetailSerializer
    lookup_field = 'id'




class AskListAPIView(ListAPIView):
    serializer_class = AskListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Ask.objects.filter(replay=None)
        # query = self.request.GET.get("search")
        # if query:
        #     queryset_list = queryset_list.filter(
        #         Q(title__icontains=query) |
        #         Q(content__icontains=query) |
        #         Q(user__username__icontains=query)
        #     ).distinct()
        return queryset_list