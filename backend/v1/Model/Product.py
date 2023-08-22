from django.db import models

from user_management.Model import UserModel


class ProductModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(blank=True, none=True, default=None)
    updated_by = models.ForeignKey(UserModel, blank=True, none=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    deleted_by = models.ForeignKey(UserModel, blank=True, none=True, default=None, on_delete=models.CASCADE)
