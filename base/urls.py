from django.contrib import admin
from django.urls import path, include

from . import views
from .views import ProductAPIList

urlpatterns = [
    path('', views.home_view),
    path('article/list/', ProductAPIList.as_view())
]