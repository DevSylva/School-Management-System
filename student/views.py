from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .serializers import StudentProfileSerializer
from rest_framework.response import Response
# Create your views here.


class StudentProfileView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        studentProfileSerializer = StudentProfileSerializer(data=request.data)
        if studentProfileSerializer.is_valid():
            newUser = studentProfileSerializer.save()
            if newUser:
                data = {
                    "data": studentProfileSerializer.data
                }
                print(request.user)
                print(request.id(newUser))
                print(data)
                return Response(data, status=status.HTTP_201_CREATED)
        return Response(studentProfileSerializer.errors, status=status.HTTP_400_BAD_REQUEST)