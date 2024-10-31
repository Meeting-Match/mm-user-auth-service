from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
