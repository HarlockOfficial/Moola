from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import SupermarketModel


class SupermarketSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = SupermarketModel
        fields = '__all__'
