from django.shortcuts import render
from rest_framework import generics, filters

from .models import Code
from .serializer import EcodeSerializer


# Create your views here.
class EcodeAPIList(generics.ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = EcodeSerializer

    search_fields = ['name', 'description', ]
    filter_backends = (filters.SearchFilter,)