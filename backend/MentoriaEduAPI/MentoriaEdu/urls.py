from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("users.urls")),

    path(
        "api/auth/token/",
        TokenObtainPairView.as_view(),
        name="token",
    ),
    path(
        "api/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "api/courses/", 
        include("courses.urls"),
    ),
]