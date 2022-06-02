from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def validate(self, attrs):
        """

        :param attrs:
        :return:
        """
        username = attrs.get('username')
        email = attrs.get('email')
        if not username.isalnum():
            raise serializers.ValidationError('The username is only alphanumeric character')
        return super().validate(attrs)

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    tokens = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise AuthenticationFailed('Account disable, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('email in not verified')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        # return super().validate(attrs)
