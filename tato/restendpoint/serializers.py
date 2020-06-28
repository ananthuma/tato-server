from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserInfo,Status


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'about', 'userId','active','password','salt','dob','phone' ,'imgurl']

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['statusId', 'userId', 'visibility', 'url', 'text', 'time', 'category']