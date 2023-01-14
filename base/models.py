from django.db import models

from django.db import models


class ProductGen(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    background = models.ImageField(null=True, upload_to='back_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Топ 10 продукт"
        verbose_name_plural = "Топ 10 продукты"


class ProductList(models.Model):
    name = models.CharField(max_length=200, null=True)
    products = models.ManyToManyField(ProductGen, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductItem(models.Model):
    prod = models.ManyToManyField(ProductList, related_name='prod')
    description = models.TextField()
    status = models.CharField(max_length=300)
    img = models.ImageField(null=True, upload_to='product_images/')

    def __str__(self):
        return self.prod

    class Meta:
        verbose_name = "Информация про продукт"
        verbose_name_plural = "Информация про продукты"




"""
{
            "createdAt": "2023-01-05T04:37:59.028+00:00",
            "updatedAt": "2023-01-05T04:37:59.028+00:00",
            "id": "c8a3b084-a236-49c4-9251-5b4b06a1f660",
            "title": "top 10 sodas",
            "background ": "file/image/b6fb13",
            "products": {
                "product1": {
                    "name":"Fanta",
                    "description": "why it's not lorem",
                    "status": "lorem",
                    "img": "file/image/b6fb13",
                },
                "product2": "Fanta",
                "product3": "Fanta",
                "product4": "Fanta",
                "product5": "Fanta",
                "product6": "Fanta",
                "product7": "Fanta",
                "product8": "Fanta",
                "product9": "Fanta",
                "product10": "Fanta",
            },
},
"""


