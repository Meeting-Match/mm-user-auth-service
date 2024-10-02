from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import User

# Create your views here.


def hello(request):
    return JsonResponse({"message": "Hello, frontend! I am the auth backend."})


def index(request):
    return HttpResponse("Hello, world!")


def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass
