from django.db import models

from user_management.Model import UserModel


class SupermarketProductPriceModel(models.Model):
    supermarket = models.ForeignKey('SupermarketModel', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ingredients = models.TextField(null=True, blank=True)
    intolerances = models.TextField(null=True, blank=True)
    allergens = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('supermarket', 'product')
        ordering = ('supermarket', 'product')