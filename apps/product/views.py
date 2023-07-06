from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer