from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView, UserInfoView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userinfo/', UserInfoView.as_view(), name='user-info'),
]
