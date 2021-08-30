from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Diary
from .serializer import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
