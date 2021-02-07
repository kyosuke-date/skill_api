from rest_framework import serializers
from .models import Category, Skills
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'dept']


class SkillsSerializer(serializers.ModelSerializer):
    dept_name = serializers.ReadOnlyField(source='dept.dept', read_only=True)
    owner_username = serializers.ReadOnlyField(source='owner.username', read_only=True)

    created_at = serializers.DateTimeField(format="%Y-%m-%-d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%-d %H:%M", read_only=True)

    class Meta:
        model = Skills
        fields = ['id', 'name', 'dept', 'dept_name', 'career', 'infla',
                  'dev', 'speciality', 'myself', 'owner', 'owner_username',
                  'created_at', 'updated_at']
        extra_kwargs = {'owner': {'read_only': True}}
