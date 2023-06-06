from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = ['id', 'name', 'description', 'category', 'slug', 'price', 'new_price', 'image',]