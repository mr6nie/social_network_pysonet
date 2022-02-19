from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from .yasg import urlpatterns as yasg

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/v1/users/", include("apps.profiles.urls")),
    path("api/v1/wall/", include("apps.wall.urls")),
    path("api/v1/follower/", include("apps.followers.urls")),
]
urlpatterns += yasg

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
