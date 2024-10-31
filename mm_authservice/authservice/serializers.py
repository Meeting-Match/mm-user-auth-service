from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.reverse import reverse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'links']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_links(self, obj):
        return [
            {
                'rel': 'self',
                'href': reverse('register', request=self.context['request']),
            },
            {
                'rel': 'token',
                'href': reverse('token_obtain_pair', request=self.context['request']),
            },
        ]


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        return [
            {
                'rel': 'self',
                'href': reverse('token_obtain_pair', request=self.context['request']),
            },
            {
                'rel': 'register',
                'href': reverse('register', request=self.context['request']),
            },
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims here, if needed
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['links'] = self.get_links()
        return data

    def get_links(self):
        return [
            {
                'rel': 'self',
                'href': reverse('token_obtain_pair', request=self.context['request']),
            },
            {
                'rel': 'register',
                'href': reverse('register', request=self.context['request']),
            },
        ]
