from django.shortcuts import render
from rest_framework import generics

from .models import Code
from .serializer import EcodeSerializer


# Create your views here.
class EcodeAPIList(generics.ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = EcodeSerializer