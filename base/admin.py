from django.contrib import admin

from .models import ProductList, ProductGen, ProductItem

admin.site.register(ProductGen)
admin.site.register(ProductList)
admin.site.register(ProductItem)


