from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import ReviewModel
from v1.Serializer import ProductSerializer


class ReviewSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    deleted_by = UserSerializer(read_only=True)

    class Meta:
        model = ReviewModel
        fields = '__all__'
