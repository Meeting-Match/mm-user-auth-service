from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView, UserInfoView
from rest_framework_simplejwt.views import TokenRefreshView
import logging

logger = logging.getLogger('authservice')

logger.info('Setting up URL patterns for the authentication service.')

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userinfo/', UserInfoView.as_view(), name='user-info'),
]

logger.info(f'Registered URL patterns: {[pattern.name for pattern in urlpatterns if pattern.name]}')