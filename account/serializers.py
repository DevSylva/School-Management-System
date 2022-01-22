from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=68, min_length=4, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def validate(self, attrs):
        username = attrs.get('username', '')

        if not username:
            raise serializers.ValidationError("User must have a username")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

