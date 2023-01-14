from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['name', 'description', 'status', 'img']


class ProductListSerializer(serializers.ModelSerializer):
    prod = ProductItemSerializer(many=True)

    class Meta:
        model = ProductList
        fields = ['prod']


class ProductGenSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = ProductGen
        fields = ['title', 'created_at', 'update_at', 'background', 'products']



