from django.contrib import admin
from django.urls import path, include

from .views import EcodeAPIList

urlpatterns = [
    path('', EcodeAPIList.as_view())
]