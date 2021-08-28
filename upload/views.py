import django_filters
from rest_framework import viewsets, filters

from .models import User, Content
from .serializer import UserSerializer, ContentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
