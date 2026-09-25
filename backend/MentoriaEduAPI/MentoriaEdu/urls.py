from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

   path("api/auth/token/", TokenObtainPairView.as_view()),
   path("api/auth/token/refresh/", TokenRefreshView.as_view()),
]