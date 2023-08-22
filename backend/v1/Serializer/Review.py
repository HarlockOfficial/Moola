from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import Review
from v1.Serializer import ProductSerializer


class ReviewSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
