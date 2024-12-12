from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView, UserInfoView, RequestUserInfoView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userinfo/<int:user_id>/', UserInfoView.as_view(), name='user-info'),
    path('userinfo/', RequestUserInfoView.as_view(), name='request-user-info'),
]
