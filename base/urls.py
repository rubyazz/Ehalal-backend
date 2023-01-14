from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import ProductAPIList

urlpatterns = [
    path('', views.home_view),
    path('article/list/', ProductAPIList.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)