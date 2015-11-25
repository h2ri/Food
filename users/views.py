from .serializers import UserInfoSerializer
from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status, viewsets,permissions
from .tools import get_access_token
from django.http import HttpResponse
from social.apps.django_app.utils import psa
from .models import MyUser, UserInfo
from rest_framework.views import APIView
from django.http import JsonResponse
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    #queryset = UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserInfo.objects.all()
        else:
            return UserInfo.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)

# Create your views here.
@psa('social:complete')
def register_by_access_token(request, backend):
    token = request.GET.get('access_token')
    phone = request.GET.get('phone')
    email = request.GET.get('email')

    try:
        user = request.backend.do_auth(token)

        print user
        if user:
            login(request, user)

            u = MyUser.objects.get(id = user.id)
            if email:
                u.email = email
                u.save()
            if phone:
                u.phone = phone
                u.save()
            return get_access_token(user,phone,email)
        else:
            return Response("asd",status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return HttpResponse(e,status=status.HTTP_404_NOT_FOUND)

