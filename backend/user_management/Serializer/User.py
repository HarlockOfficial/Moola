from rest_framework.serializers import ModelSerializer

from user_management.Model import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser']
