from django.db import models

from user_management.Model import UserModel


class SupermarketModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
