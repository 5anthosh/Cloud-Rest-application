from rest_framework import serializers
from .models import Field, FieldHistory


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('data', 'field_name',)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldHistory
        fields = ('time', 'data',)
