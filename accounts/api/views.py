
from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
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

from news.api.permissions import IsOwnerOrReadOnly
# from news.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from accounts.models import UserProfile



User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
UserProfileSerializer,
)


class UserProfileModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    # permission_classes = [IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    lookup_field = 'username'



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



















