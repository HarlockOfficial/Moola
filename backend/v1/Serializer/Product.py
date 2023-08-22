from user_management.Serializer import UserSerializer
from v1.Model import ProductModel

from rest_framework.serializers import ModelSerializer, ImageField


class ProductSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    deleted_by = UserSerializer(read_only=True)
    image = ImageField(use_url=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
