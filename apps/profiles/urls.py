from django.urls import path

from .views import GetUserNetView

urlpatterns = [
    path("<int:pk>", GetUserNetView.as_view(), name="user_info"),
]
