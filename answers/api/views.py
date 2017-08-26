from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from news.api.pagination import  PostPageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from answers.models import Answer
from .serializers import (
    AnswerDetailSerializer,
    AnswerListSerializer,
    AnswerCreateUpdateSerializer,
)
class AnswerCreateAPIView(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save()


class AnswerDetailAPIView(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer
    lookup_field = 'slug'

class AnswerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateUpdateSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAdminUser]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class AnswerDeleteAPIView(DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer
    lookup_field = 'slug'


class AnswerListAPIView(ListAPIView):
    serializer_class = AnswerListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Answer.objects.filter(wait=False)
        query = self.request.GET.get("search")
        type = self.request.GET.get("type")
        wait = self.request.GET.get("wait")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        if type:
            print type
            queryset_list = queryset_list.filter(type=type)
        if wait:
            if wait == "true" or wait == "True":
                queryset_list = queryset_list.filter(wait=True)
        return queryset_list


# class AnswerWaitListAPIView(ListAPIView):
#     serializer_class = AnswerListSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ["title", "content"]
#     pagination_class = PostPageNumberPagination
#
#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Answer.objects.filter(wait=True)
#         query = self.request.GET.get("search")
#         if query:
#             queryset_list = queryset_list.filter(
#                 Q(title__icontains=query) |
#                 Q(content__icontains=query) |
#                 Q(user__username__icontains=query)
#             ).distinct()
#         return queryset_list