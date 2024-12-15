from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer
import logging

logger = logging.getLogger('authservice')

def get_correlation_id(request):
    return getattr(request, 'correlation_id', 'N/A')

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        correlation_id = get_correlation_id(request)
        logger.info(f'User registration request received with data: {request.data}', extra={'correlation_id': correlation_id})
        
        try:
            response = super().create(request, *args, **kwargs)
            response.data['links'] = response.data.pop('links')
            logger.info(f'User registered successfully with ID: {response.data.get('id')}', extra={'correlation_id': correlation_id})
            return response
        except Exception as e:
            logger.error(f'Error during user registration: {e}', extra={'correlation_id': correlation_id})
            return Response({'error': 'Registration failed'}, status=500)


class UserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        correlation_id = get_correlation_id(request)
        logger.info(f'User info request received for user: {request.user}', extra={'correlation_id': correlation_id})
        
        user = request.user
        response_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        logger.info(f'User info retrieved successfully for user ID: {user.id}', extra={'correlation_id': correlation_id})
        return Response(response_data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        correlation_id = get_correlation_id(request)
        logger.info(f'Token request received with data: {request.data}', extra={'correlation_id': correlation_id})
        
        try:
            response = super().post(request, *args, **kwargs)
            response.data['links'] = response.data.pop('links')
            logger.info(f'Token generated successfully', extra={'correlation_id': correlation_id})
            return response
        except Exception as e:
            logger.error(f'Error during token generation: {e}', extra={'correlation_id': correlation_id})
            return Response({'error': 'Token generation failed'}, status=500)
