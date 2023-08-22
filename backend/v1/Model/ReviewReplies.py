from django.db import models

from user_management.Model import UserModel


class ReviewRepliesModel(models.Model):
    # NOTE: either review or other_reply has to be filled, enforce this in the Controller
    review = models.ForeignKey('ReviewModel', on_delete=models.CASCADE, null=True, blank=True)
    other_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
