from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshSlidingView

from .views import CustomUserViewSet, CustomTokenObtainSlidingView
from .models import CustomUserManager, CustomUser

router = routers.DefaultRouter()
router.register('user', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/',CustomUserManager.create_user),
    path('token/', CustomTokenObtainSlidingView.as_view()),
    path('token-refresh/', TokenRefreshSlidingView.as_view()),
]
