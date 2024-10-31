
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
