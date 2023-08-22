from django.contrib import admin

from v1.Model import ProductModel, ReviewModel, ReviewRepliesModel, SupermarketModel, SupermarketProductPriceModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(ReviewModel)
admin.site.register(ReviewRepliesModel)
admin.site.register(SupermarketModel)
admin.site.register(SupermarketProductPriceModel)
