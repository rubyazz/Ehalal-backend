from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializer import ProductGenSerializer, ProductListSerializer


def home_view(request):
    return JsonResponse({'success':True, 'message':'Welcome to our app'})


class ProductAPIList(generics.ListCreateAPIView):
    queryset = ProductGen.objects.all()
    serializer_class = ProductGenSerializer