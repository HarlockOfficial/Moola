from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import SupermarketProductPrice
from v1.Serializer import ProductSerializer, SupermarketSerializer


class SupermarketProductPriceSerializer(ModelSerializer):
    supermarket = SupermarketSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = SupermarketProductPrice
        fields = '__all__'
