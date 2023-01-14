from django.contrib import admin

from .models import ProductList, ProductGen, ProductItem, Category, Code

admin.site.register(ProductGen)
admin.site.register(ProductList)
admin.site.register(ProductItem)
admin.site.register(Code)
admin.site.register(Category)

