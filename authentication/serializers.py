from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

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
