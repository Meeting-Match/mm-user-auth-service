from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer, UserSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        response = super().create(request, *args, **kwargs)
        response.data['links'] = response.data.pop('links')
        return response


class RequestUserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Check if user is authenticated
        if not user or not user.is_authenticated:
            raise AuthenticationFailed("User not authenticated")

        # Build the response
        user_info = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

        return Response(user_info)


class UserInfoView(APIView):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get(self, request, user_id=None):
        # If no user_id is provided, use the authenticated user
        if user_id is None:
            user = request.user
        else:
            # Retrieve the specified user
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=404)

        # Use the serializer to convert the user object
        serializer = self.serializer_class(user, context={'request': request})
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        print("Processing post request")
        print(request.data)
        response = super().post(request, *args, **kwargs)
        response.data['links'] = response.data.pop('links')
        return response
