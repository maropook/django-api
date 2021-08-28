from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Content


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'img')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'body', 'created_at', 'status', 'author')
