from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tato.restendpoint.serializers import UserSerializer, StatusSerializer
from tato.restendpoint.serializers import UserInfoSerializer
from tato.restendpoint.models import UserInfo, Status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('name')
    serializer_class = UserInfoSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().order_by('statusId')
    serializer_class = StatusSerializer
