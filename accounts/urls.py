from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import UserViewSet, signup, logout
from django.urls import path

from rest_framework import routers

r = routers.SimpleRouter()
r.register(r"users", UserViewSet)

urlpatterns = [
    path("auth/signup/", signup, name="signup"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/logout/", logout, name="logout"),
] + r.urls
