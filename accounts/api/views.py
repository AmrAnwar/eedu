from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)
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


class UserLogoutAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('id'))
        if user.profile.login:
            user.profile.login = False
            user.profile.save()
            return Response(data={'detail': 'logout successfully'}, status=HTTP_200_OK)
        return Response(data={'detail': 'logout fail'}, status=HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            user = User.objects.get(username=new_data.get('username'))
            user.profile.login = True
            user.profile.save()
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



















