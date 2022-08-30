from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many = False)
    class Meta:
        model = Product
        fields = ['name', 'subcategory', 'description', 'price']

