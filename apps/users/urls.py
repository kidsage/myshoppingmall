from django.urls import path

from core.urls import viewset_path
from apps.users.views import UserViewSet, UserProfileViewSet


urlpatterns = [
    viewset_path(UserViewSet, "users"),
    viewset_path(UserProfileViewSet, "profile"),
]