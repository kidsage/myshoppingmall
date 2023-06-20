from django.urls import path

from core.urls import viewset_path
from apps.users.views import UserViewSet


urlpatterns = [
    viewset_path(UserViewSet, "users"),
]