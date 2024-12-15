from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.reverse import reverse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import logging

logger = logging.getLogger('authservice')

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'links']

    def create(self, validated_data):
        correlation_id = self.context.get('correlation_id', 'N/A')
        logger.info(f'Creating a new user with username: {validated_data['username']}', extra={'correlation_id': correlation_id})

        try:
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            logger.info(f'User created successfully with ID: {user.id}', extra={'correlation_id': correlation_id})
            return user
        except Exception as e:
            logger.error(f'Error creating user: {e}', extra={'correlation_id': correlation_id})
            raise serializers.ValidationError('User creation failed')

    def get_links(self, obj):
        correlation_id = self.context.get('correlation_id', 'N/A')
        logger.debug(f'Generating links for user ID: {obj.id}', extra={'correlation_id': correlation_id})
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        correlation_id = cls.context.get('correlation_id', 'N/A') if hasattr(cls, 'context') else 'N/A'
        logger.info(f'Generating token for user ID: {user.id}', extra={'correlation_id': correlation_id})
        token = super().get_token(user)
        # Add custom claims here, if needed
        return token

    def validate(self, attrs):
        correlation_id = self.context.get('correlation_id', 'N/A')
        logger.info(f'Validating token for user with username: {attrs.get('username')}', extra={'correlation_id': correlation_id})

        try:
            data = super().validate(attrs)
            data['links'] = self.get_links()
            logger.info(f'Token validated successfully for username: {attrs.get('username')}', extra={'correlation_id': correlation_id})
            return data
        except Exception as e:
            logger.error(f'Error during token validation: {e}', extra={'correlation_id': correlation_id})
            raise serializers.ValidationError('Token validation failed')

    def get_links(self):
        correlation_id = self.context.get('correlation_id', 'N/A')
        logger.debug('Generating token-related links', extra={'correlation_id': correlation_id})
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
