from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=4, write_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'is_student']

    def validate(self, attrs):
        email = attrs.get('email', '')

        if not email:
            raise serializers.ValidationError("User must have an Email")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

