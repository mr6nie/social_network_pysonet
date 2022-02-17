from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as yasg

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/", include("apps.profiles.urls")),
]

urlpatterns += yasg
