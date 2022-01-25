from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import RegisterUserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse


User = get_user_model()

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newUser = reg_serializer.save()
            if newUser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)