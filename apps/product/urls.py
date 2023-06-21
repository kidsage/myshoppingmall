from django.urls import path

from core.urls import viewset_path
from apps.product.views import ProductViewSet


urlpatterns = [
    viewset_path(ProductViewSet, "product"),
]