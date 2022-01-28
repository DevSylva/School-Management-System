from rest_framework import serializers
from .models import Student
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class StudentProfileSerializer(serializers.ModelSerializer):
    first_name    = serializers.CharField(max_length=16)
    last_name     = serializers.CharField(max_length=16)
    reg_number    = serializers.CharField(max_length=8)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'reg_number', 'gender', 'phone_number']

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name  = attrs.get('last_name', '')
        reg_number = attrs.get('reg_number', '')

        if not reg_number:
            raise serializers.ValidationError('The student registration number should be provided.')
            return reg_number.upper()
        return attrs

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
