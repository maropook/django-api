from django.db.models import fields
from rest_framework import serializers

from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'


# モデルに対応するserializerを作成する．fieldsに与えるのはAPIとして出力したいフィールド名のタプル
# fieldsに列挙したものはシリアライズして出力される
