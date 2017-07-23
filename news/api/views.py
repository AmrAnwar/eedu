from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from news.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostDetailSerializer,
    PostListSerializer,
    PostCreateUpdateSerializer,
)
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.filter(wait=False)
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
            if wait=="true" or wait =="True":
                queryset_list = queryset_list.filter(wait=True)
        return queryset_list


class PostWaitListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.filter(wait=True)
        query = self.request.GET.get("search")
        if query:
            print query
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        return queryset_list
