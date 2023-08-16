from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    REQUIRED_FIELDS = ['username', 'password']
