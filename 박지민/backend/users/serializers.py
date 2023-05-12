from rest_framework import serializers
from .models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'hobby']


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
