from user_management.Serializer import UserSerializer
from v1.Model import Product

from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'