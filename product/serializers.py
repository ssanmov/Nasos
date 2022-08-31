from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer
    class Meta:
        model = Subcategory
        fields = ['id','name', 'category','category_id']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many = False)
    class Meta:
        model = Product
        fields = ['id','name','image', 'subcategory', 'description', 'price']

