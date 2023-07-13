from django.contrib import admin
from .models import ProductList, ProductGen, ProductItem


@admin.register(ProductGen)
class ProductGenAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at',]
    list_filter = ['created_at',]  # Corrected field name
    search_fields = ['title',]
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at',]  # Corrected field name


@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_product_list', 'status']
    list_filter = ['status']
    search_fields = ['name', 'prod__name']
    filter_horizontal = ['prod']
    readonly_fields = ['get_product_list']

    def get_product_list(self, obj):
        return ", ".join([p.name for p in obj.prod.all()])

    get_product_list.short_description = 'Product List'

