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


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        response = super().create(request, *args, **kwargs)
        response.data['links'] = response.data.pop('links')
        return response


class UserInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        print("Processing post request")
        print(request.data)
        response = super().post(request, *args, **kwargs)
        response.data['links'] = response.data.pop('links')
        return response
